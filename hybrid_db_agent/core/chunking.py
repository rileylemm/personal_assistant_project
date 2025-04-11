import re
import logging
import os
import sys
from typing import List, Dict, Any, Tuple, Optional

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('chunking')

class Chunk:
    """
    Represents a chunk of text from a document with metadata.
    """
    def __init__(self, text: str, metadata: Dict[str, Any]):
        self.text = text
        self.metadata = metadata
    
    def __repr__(self):
        return f"Chunk(text='{self.text[:50]}...', metadata={self.metadata})"

class MarkdownChunker:
    """
    Chunker for Markdown documents that respects header structure.
    """
    # Regular expressions for finding headers and their levels
    HEADER_PATTERN = re.compile(r'^(#{1,6})\s+(.*?)$', re.MULTILINE)
    
    def __init__(
        self,
        min_chunk_size: int = Config.PROCESSING.CHUNK_MIN_SIZE,
        max_chunk_size: int = Config.PROCESSING.CHUNK_MAX_SIZE,
        chunk_overlap: int = Config.PROCESSING.CHUNK_OVERLAP
    ):
        """
        Initialize the markdown chunker.
        
        Args:
            min_chunk_size: Minimum size of a chunk in characters
            max_chunk_size: Maximum size of a chunk in characters
            chunk_overlap: Number of characters to overlap between chunks
        """
        self.min_chunk_size = min_chunk_size
        self.max_chunk_size = max_chunk_size
        self.chunk_overlap = chunk_overlap
        logger.info(f"Initialized MarkdownChunker with min_size={min_chunk_size}, max_size={max_chunk_size}, overlap={chunk_overlap}")
    
    def chunk_document(self, document_text: str, document_metadata: Dict[str, Any]) -> List[Chunk]:
        """
        Split a markdown document into chunks based on headers and content.
        
        Args:
            document_text: The markdown text to chunk
            document_metadata: Metadata about the document (id, filename, etc.)
            
        Returns:
            List of Chunk objects
        """
        logger.info(f"Chunking document with id: {document_metadata.get('document_id', 'unknown')}")
        
        # Extract sections based on headers
        sections = self._extract_sections(document_text)
        
        # Convert sections to chunks
        chunks = self._sections_to_chunks(sections, document_metadata)
        
        logger.info(f"Created {len(chunks)} chunks from document")
        return chunks
    
    def _extract_sections(self, text: str) -> List[Dict[str, Any]]:
        """
        Extract markdown sections based on headers.
        
        Args:
            text: Markdown text
            
        Returns:
            List of section dictionaries with header info and content
        """
        # Find all headers in the document
        headers = list(self.HEADER_PATTERN.finditer(text))
        
        if not headers:
            # If no headers found, treat the entire document as one section
            return [{
                'level': 0,
                'title': 'Document',
                'content': text,
                'start': 0,
                'end': len(text)
            }]
        
        sections = []
        
        # Process each header and its content
        for i, header_match in enumerate(headers):
            # Determine header level by counting # symbols
            level = len(header_match.group(1))
            title = header_match.group(2).strip()
            start = header_match.start()
            
            # Find the end of this section (start of next header or end of text)
            if i < len(headers) - 1:
                end = headers[i + 1].start()
            else:
                end = len(text)
            
            # Extract section content (excluding the header itself)
            content = text[header_match.end():end].strip()
            
            # Add section to list
            sections.append({
                'level': level,
                'title': title,
                'content': content,
                'start': start,
                'end': end
            })
        
        return sections
    
    def _sections_to_chunks(self, sections: List[Dict[str, Any]], document_metadata: Dict[str, Any]) -> List[Chunk]:
        """
        Convert markdown sections to chunks, respecting max chunk size.
        
        Args:
            sections: List of section dictionaries
            document_metadata: Metadata about the document
            
        Returns:
            List of Chunk objects
        """
        chunks = []
        
        for section in sections:
            # Create metadata for this section
            section_metadata = document_metadata.copy()
            section_metadata.update({
                'header_level': section['level'],
                'header_title': section['title'],
                'section_start': section['start'],
                'section_end': section['end']
            })
            
            content = section['content']
            
            # If content is short enough, create a single chunk
            if len(content) <= self.max_chunk_size:
                if len(content) >= self.min_chunk_size or section['level'] > 0:
                    chunks.append(Chunk(content, section_metadata))
                continue
            
            # Split large sections into smaller chunks
            chunk_texts = self._split_text(content, self.max_chunk_size, self.chunk_overlap)
            
            for i, chunk_text in enumerate(chunk_texts):
                chunk_metadata = section_metadata.copy()
                chunk_metadata.update({
                    'chunk_index': i,
                    'total_chunks': len(chunk_texts)
                })
                chunks.append(Chunk(chunk_text, chunk_metadata))
        
        return chunks
    
    def _split_text(self, text: str, max_size: int, overlap: int) -> List[str]:
        """
        Split text into chunks of maximum size with overlap.
        
        Args:
            text: Text to split
            max_size: Maximum chunk size
            overlap: Overlap between chunks
            
        Returns:
            List of text chunks
        """
        if len(text) <= max_size:
            return [text]
        
        chunks = []
        start = 0
        
        while start < len(text):
            # Determine end of current chunk
            end = start + max_size
            
            if end >= len(text):
                # Last chunk
                chunks.append(text[start:])
                break
            
            # Try to find a paragraph break for a more natural split
            paragraph_break = text.rfind('\n\n', start, end)
            
            if paragraph_break != -1 and paragraph_break > start + self.min_chunk_size:
                # Split at paragraph break
                chunks.append(text[start:paragraph_break].strip())
                start = paragraph_break
            else:
                # Split at max_size
                chunks.append(text[start:end].strip())
                start = end - overlap
        
        return chunks

# Example usage
if __name__ == "__main__":
    # Test with a sample markdown document
    sample_md = """# Introduction
    
This is an introduction paragraph that explains the purpose of this document.

## Background

Some background information about the topic.

### Detailed Background

More detailed information that dives deeper into the specific aspects of the background.

## Methodology

This section describes the methodology used.

# Results

Here are the results of our analysis.

## Discussion

Let's discuss what these results mean.
"""
    
    chunker = MarkdownChunker()
    chunks = chunker.chunk_document(sample_md, {'document_id': 'test-doc', 'filename': 'test.md'})
    
    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}:")
        print(f"  Metadata: {chunk.metadata}")
        print(f"  Text: {chunk.text[:100]}...")
        print() 