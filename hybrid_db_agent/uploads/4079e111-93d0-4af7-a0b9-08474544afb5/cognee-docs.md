This file is a merged representation of a subset of the codebase, containing files not matching ignore patterns, combined into a single document by Repomix. The content has been processed where security check has been disabled.

# File Summary

## Purpose
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching these patterns are excluded: content/_meta.js
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Security check has been disabled - content may contain sensitive information

## Additional Info

# Directory Structure
```
content/
  core-concepts/
    _meta.ts
    architecture.mdx
    chunking.mdx
    data-ingestion.mdx
    data-management-crud.mdx
    graph-generation.mdx
    ontologies.mdx
    pipelines.mdx
  how-to-guides/
    deployment/
      _meta.js
      helm.mdx
      mcp.mdx
      modal.mdx
    optimization/
      _meta.js
      descriptive-metrics.mdx
      evaluation-framework.mdx
    _meta.js
    cognee-tasks.mdx
    configuration.mdx
    deployment.mdx
    graph-visualization.mdx
    local-models.mdx
    own-data-model.mdx
    remote-models.mdx
    search.mdx
  integrations/
    _meta.js
    cline.mdx
    continue.mdx
    cursor.mdx
    roo-code.mdx
  reference/
    _meta.js
    api-reference.mdx
    colab-notebooks.mdx
    descriptive-metrics.mdx
    infrastructure.mdx
    modules.mdx
    ontology-reference.mdx
    retriever-evaluation.mdx
    sdk.mdx
    search-types.mdx
    tasks.mdx
  tutorials/
    load-your-data.mdx
    turn-your-repo-into-graph.mdx
    use-ontology.mdx
    use-the-api.mdx
    user-authentication.mdx
  use-cases/
    chatbots.mdx
    code-assistants.mdx
    human-resources.mdx
  core-concepts.mdx
  how-to-guides.mdx
  index.mdx
  integrations.mdx
  quickstart.mdx
  reference.mdx
  research.mdx
  resources.mdx
  tutorials.mdx
  use-cases.mdx
```

# Files

## File: content/core-concepts/_meta.ts
````typescript
import { MetaRecord } from "nextra";

const meta: MetaRecord = {
  architecture: "Architecture",
  pipelines: "Pipelines",
  chunking: "Chunking",
  "data-ingestion": "Data Ingestion",
  "graph-generation": "Graph Generation",
  ontologies: "Ontologies",
  "data-management-crud": "Data Management (CRUD)",
}

export default meta;
````

## File: content/core-concepts/architecture.mdx
````
---
title: Architecture
---

export function generateMetadata() {
  return {
    title: "Cognee - Architecture",
    description: "Read about pipelines and tasks and how we use them in cognee.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/core-concepts/architecture",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/core-concepts/architecture",
      type: "website",
      title: "Cognee - Architecture",
      description: "Read about pipelines and tasks and how we use them in cognee.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee - Architecture",
      description: "Read about pipelines and tasks and how we use them in cognee.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}

# Cognee Architecture Overview

The Cognee architecture centers around tasks, pipelines, and typed data points, working together to transform raw data into meaningful knowledge graphs.

Cognification Process
![Cognification Process](/images/architecture/high-level-architecture.webp)

Cognee Architecture
![Cognee Architecture](/images/architecture/low-level-architecture.webp)
````

## File: content/core-concepts/chunking.mdx
````
---
title: Chunking text with cognee
---

export function generateMetadata() {
  return {
    title: "Cognee - Chunking text with cognee",
    description: "Split text into smaller units called chunks. Cognee supports external chunkers + we maintain some ourselves.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/core-concepts/chunking",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/core-concepts/chunking",
      type: "website",
      title: "Cognee - Chunking text with cognee",
      description: "Split text into smaller units called chunks. Cognee supports external chunkers + we maintain some ourselves.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee - Chunking text with cognee",
      description: "Split text into smaller units called chunks. Cognee supports external chunkers + we maintain some ourselves.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}

# Chunking text with cognee

Chunking is the process of splitting text into smaller, more manageable units (referred to as “chunks”). These chunks form the foundation for downstream tasks such as embedding, classification, and ultimately the construction of a knowledge graph. Cognee’s flexible chunking approach ensures that no matter the data source—documents, code snippets, or web content—you can tailor chunking logic to fit your needs.

## Why Chunking Matters

- **Manageability:**
  Large documents are hard to handle as single units. Splitting them into smaller pieces allows more granular analysis.

- **Improved Quality of Embeddings and Classification:**
  LLMs and vector databases often perform better when dealing with shorter, more focused pieces of text. Chunked data ensures embeddings capture more specific semantic information.

- **Contextual Relevance:**
  By working with smaller data units, Cognee can more accurately identify relevant facts and relationships, improving the overall quality of retrieval-augmented generation (RAG) results.

## How Cognee Handles Chunking

In Cognee, chunking can be implemented as a **Task** within a **Pipeline**. The chunking task receives a `Datapoint` (e.g., `DocumentData` containing raw text) and returns another `Datapoint` (e.g., `ChunkData` with a list of text chunks).

### Key Concepts

- **Tasks:**
  A `ChunkingTask` is responsible for performing the actual splitting of text. Different tasks can implement different splitting logic—by paragraphs, sentences, tokens, or custom delimiters.

- **Datapoints:**
  A `pydantic`-based model (e.g., `ChunkData`) defines the schema for the output of the chunking process, ensuring all subsequent tasks receive the data in a known, structured format.

- **Integration in Pipelines:**
  Chunking typically appears early in a pipeline, after text ingestion but before embedding and entity extraction. By chunking first, you ensure that all downstream tasks process consistently sized units of information.

## Example Code Snippet

Below is a simplified example of a chunking task and how it might be integrated into a pipeline.

```python
import cognee
import asyncio
from pydantic import BaseModel
from cognee import Task, Pipeline

# Define Datapoints
class DocumentData(BaseModel):
    content: str

class ChunkData(BaseModel):
    chunks: list[str]

# Define a simple chunking task
class ChunkingTask(Task):
    def run(self, doc: DocumentData) -> ChunkData:
        # Example: split by double newlines
        chunks = doc.content.split("\n\n")
        return ChunkData(chunks=chunks)

async def main():
    # Reset Cognee state
    await cognee.prune.prune_data()
    await cognee.prune.prune_system(metadata=True)

    text = """
    Natural language processing (NLP) is an interdisciplinary
    subfield of computer science and information retrieval.

    NLP techniques are used to analyze text, allowing machines to
    understand human language.
    """

    # Add text to Cognee
    await cognee.add(text)

    # Create a pipeline with just the chunking task for demonstration
    chunking_pipeline = Pipeline([ChunkingTask()])

    # Retrieve the added document from Cognee as DocumentData
    # (In practice, this might be part of a pipeline or a retrieval task.)
    doc_data = DocumentData(content=text.strip())

    # Run the pipeline to chunk the document
    chunk_data = chunking_pipeline.run(doc_data)
    print("Chunks:", chunk_data.chunks)

if __name__ == '__main__':
    asyncio.run(main())
````

## File: content/core-concepts/data-ingestion.mdx
````
---
title: Data Ingestion
---

export function generateMetadata() {
  return {
    title: "Cognee - Data Ingestion",
    description: "Cognee ingests data from 30+ sources.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/core-concepts/data-ingestion",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/core-concepts/data-ingestion",
      type: "website",
      title: "Cognee - Data Ingestion",
      description: "Cognee ingests data from 30+ sources.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee - Data Ingestion",
      description: "Cognee ingests data from 30+ sources.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}

# Why bother with data ingestion?

In order to use cognee, you need to ingest data into the cognee data store. 
This data can be events, customer data, or third-party data. 

In order to build reliable models and pipelines, we need to structure and process various types of datasets and data sources in the same way.
Some of the operations like normalization, deduplication, and data cleaning are common across all data sources.

This is where cognee comes in. It provides a unified interface to ingest data from various sources and process it in a consistent way.
For this we use dlt (Data Loading Tool) which is a part of cognee infrastructure.

# Example

Let's say you have a dataset of customer reviews in a PDF file. You want to ingest this data into cognee and use it to train a model.

You can use the following code to ingest the data:

```python
dataset_name = "artificial_intelligence"

ai_text_file_path = os.path.join(
    pathlib.Path(__file__).parent,
    "test_data/artificial-intelligence.pdf")
    
await cognee.add([ai_text_file_path], dataset_name)

```

cognee uses dlt to ingest the data and allows you to use:

1. SQL databases. Supports PostgreSQL, MySQL, MS SQL Server, BigQuery, Redshift, and more.
2. REST API generic source. Loads data from REST APIs using declarative configuration.
3. OpenAPI source generator. Generates a source from an OpenAPI 3.x spec using the REST API source.
4. Cloud and local storage. Retrieves data from AWS S3, Google Cloud Storage, Azure Blob Storage, local files, and more.



# What happens under the hood?

We use dlt as a loader to ingest data into the cognee metadata store. We can ingest data from various sources like SQL databases, REST APIs, OpenAPI specs, and cloud storage.
This enables us to have a common data model we can then use to build models and pipelines.
The models and pipelines we build in this way end up in the cognee data store, which is a unified interface to access the data.
````

## File: content/core-concepts/data-management-crud.mdx
````
---
title: Data Management (CRUD)
---

export function generateMetadata() {
  return {
    title: "Cognee - Data Management (CRUD)",
    description: "Explore data management in cognee. Learn how to add data, remove it, edit...",
    alternates: {
      canonical: "https://www.docs.cognee.ai/core-concepts/data-management-crud",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/core-concepts/data-management-crud",
      type: "website",
      title: "Cognee - Data Management (CRUD)",
      description: "Explore data management in cognee. Learn how to add data, remove it, edit...",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee - Data Management (CRUD)",
      description: "Explore data management in cognee. Learn how to add data, remove it, edit...",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}

## What is CRUD?

CRUD stands for:

1. **Create**: Add new records or data entries.
2. **Read**: Retrieve existing data (search, filter, or simply fetch details).
3. **Update**: Modify existing data, such as changing a record’s content or updating settings.
4. **Delete**: Remove data entries that are no longer needed or are incorrect.

These operations form the backbone of data management. In cognee, you’ll use CRUD concepts to add data to your datasets, retrieve them for inspection or processing, update system settings or dataset details, and remove data or entire datasets as needed.

Cognee provides a flexible way to manage data and knowledge graphs through a set of CRUD operations, aligning with standard RESTful API conventions. Now, we will walk you through how CRUD works within cognee and offer practical examples on how to integrate these operations into your workflow.

## RESTful Alignment

In a RESTful context, each HTTP method typically corresponds to one of these CRUD actions. Cognee’s API follows these conventions, making it straightforward for developers to integrate cognee into their applications or data pipelines.

| CRUD Actions | RESTful Context | How Cognee Handles |
| --- | --- | --- |
| Create | POST | **Upload** new datasets or documents for analysis |
| Read | GET | **Retrieve** the current state of datasets, graphs, and system settings |
| Update | PUT/PATCH | **Refine** configurations and reprocess data to improve AI-driven results |
| Delete | DELETE | **Clean Up** when a dataset is no longer needed or to remove specific data entries |

---

## Cognee’s Endpoints

Below is a quick reference for how these CRUD operations map to cognee’s API endpoints. You can find detailed information in [cognee’s API Reference](https://docs.cognee.ai/reference/api-reference).

### 1. Create

**Add Data**  
`POST /add`  
Upload new data (e.g., files, documents) to a specified dataset. The uploaded files will be stored and available for further processing (e.g., chunk extraction, graph population).

### 2. Read

- **Get Datasets**  
  `GET /datasets`  
  Retrieve a list of available datasets.

- **Get Dataset Data**  
  `GET /datasets/{dataset_id}/data`  
  Retrieves the data entries (documents, files, etc.) associated with a specific dataset.

- **Get Dataset Graph**  
  `GET /datasets/{dataset_id}/graph`  
  Obtain the graph visualization URL for a particular dataset. 

- **Get Dataset Status**  
  `GET /datasets/status`  
  Check the status of one or more datasets. 

- **Get Raw Data**  
  `GET /datasets/{dataset_id}/data/{data_id}/raw`  
  Downloads the original file for a specific data entry.

- **Get Settings**  
  `GET /settings`  
  Retrieves current system configurations (LLM settings, vector DB configurations, etc.).

### 3. Update

- **Save or Update Settings**  
  `POST /settings`  
  Updates system configurations. This does not modify datasets directly but affects how data is processed and stored.

### 4. Delete

- **Delete a Dataset**  
  `DELETE /datasets/{dataset_id}`  
  Removes as specific dataset by its ID, including all associated data from cognee’s storage.

#### Deleting a Single Document from a Dataset

Currently, cognee does not offer a single “delete document” endpoint for partially removing files from a dataset’s graph. However, you **can** remove a file from the dataset’s metastore using a script provided in the codebase, ensuring it will not be processed in subsequent runs:

- [`delete_data.py`](https://github.com/topoteretes/cognee/blob/main/cognee/modules/data/methods/delete_data.py)

Once removed from the metastore:
1. The file will no longer appear in the dataset listing.
2. If you re-run [`cognify`](https://docs.cognee.ai/core-concepts/pipelines#main-pipeline-cogneecognify) on that dataset, the removed file will not be included in the new graph build.

> **Note**: A feature is cooking to remove a single document from the knowledge graph itself. Until that is released, manually removing the file from the metastore is the best workaround if you do not want to delete the entire dataset.

---

## Example CRUD Workflow in cognee

A typical sequence using cognee’s RESTful API might look like this:

**1. Create** - upload your documents or data to a new dataset
   ```bash
   POST /add
   ```

**2. Read** - verify the dataset was created and inspect its contents
    
    ```bash
    GET /datasets
    GET /datasets/{dataset_id}/data
    ```
    
**3. Cognify** - once the dataset is verified, trigger cognitive processing (e.g., generate embeddings, extract knowledge graphs, etc.)
    
    ```bash
    POST /cognify
    {
      "datasets": ["..."]
    }
    ```
    
**4. Read (Graph Insights)** - check the resulting graph and insights
    
    ```bash
    GET /datasets/{dataset_id}/graph
    GET /datasets/status
    ```
    
**5. Update** - adjust system settings if necessary
    
    ```bash
    POST /settings
    {
      "llm_provider": "...",
      "vector_db": "..."
    }
    ```
    
**6. Search** - now that the dataset is processed, run queries to discover insights
    
    ```bash
    POST /search
    {
      "dataset_id": "{dataset_id}",
      "query": "...?"
    }
    ```
    
**7. Delete** - remove the dataset entirely if no longer needed
    
    ```bash
    DELETE /datasets/{dataset_id}
    ```

See an [example](/tutorials/use_the_api) with code.
    
## Cognee SDK Overview: CRUD in Practice

The cognee SDK offers a structured approach to data management through its core components, which align with CRUD operations. Here's a summary from the CRUD perspective:

**Create** -> **Data Ingestion:** `cognee.add(text: str)` adds new text data to the metastore for future graph and embedding generation.

**Read** -> **Data Retrieval:** `cognee.search(...)` searches the knowledge graph or embeddings, enabling quick data exploration.

**Update** -> **Data Processing:** `cognee.cognify()` processes ingested data, including generating embeddings and building knowledge graphs.

**Delete** -> **Data Pruning:** `cognee.prune.prune_data()` removes stored documents, embeddings, or graph elements when they are no longer relevant.

These functions let you manage the full data lifecycle within cognee, making it easier to create, read, update, and delete data elements programmatically.


---

## Join the Conversation!

For further details, please visit:

- [Cognee API Reference](https://docs.cognee.ai/reference/api-reference)
- [GitHub Repository](https://github.com/topoteretes/cognee)

If you have additional questions or suggestions, feel free to reach out on our Discord channel or open an issue in our GitHub repo.

<br></br>
<a href="https://discord.gg/m63hxKsp4p" target="_blank" rel="noopener noreferrer">
<button className="button cta-button">
Join the community
</button>
</a>
````

## File: content/core-concepts/graph-generation.mdx
````
---
title: Graph Generation
---

export function generateMetadata() {
  return {
    title: "Cognee - Graph Generation",
    description: "Cognee enables you to create, query, and manipulate knowledge graphs derived from your data.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/core-concepts/graph-generation",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/core-concepts/graph-generation",
      type: "website",
      title: "Cognee - Graph Generation",
      description: "Cognee enables you to create, query, and manipulate knowledge graphs derived from your data.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee - Graph Generation",
      description: "Cognee enables you to create, query, and manipulate knowledge graphs derived from your data.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}

# Working with Graphs in Cognee

Cognee enables you to create, query, and manipulate knowledge graphs derived from your data. Through a combination of structured pipelines, tasks, and typed DataPoints, you can transform raw textual input into rich semantic graphs that LLMs can use to produce contextually relevant responses.

This page provides a more in-depth look at how tasks and pipelines power the graph creation process. For an introductory example, see the [Getting Started](/quickstart) guide.

## Key Concepts

### Tasks

Tasks are the fundamental units of logic within Cognee’s processing model. Each task:

- **Inputs and Outputs:** Takes in specific data, processes it, and outputs a transformed result.
- **Typed Datapoints:** Uses `pydantic`-based models to ensure the input and output schemas are well-defined and validated.
- **Single Responsibility:** Typically, a task focuses on a single step of the workflow—such as extracting text chunks, embedding them, or classifying their content.

Because tasks are self-contained, it’s easy to reuse them in multiple pipelines, swap them out for improved or alternate implementations, and maintain them as independent modules within your codebase.

**Example:**
A `ChunkingTask` might accept raw document text as input and return an array of `ChunkData` objects representing smaller units of the original text.

### Pipelines

Pipelines are orchestrations of tasks designed to perform complex operations end-to-end. Instead of handling the entire process in a monolithic script, pipelines let you compose several tasks into a coherent sequence or graph of operations.

**Features of Pipelines:**

- **Composable:** By combining tasks that are each focused on a single responsibility, you can create pipelines that perform complex transformations, such as:
  - Reading documents from a store.
  - Chunking and embedding text.
  - Classifying entities and relationships.
  - Building a final knowledge graph.

- **Scalable:** As your data and complexity grow, you can easily add more tasks or rearrange existing ones within the pipeline without refactoring large portions of code.

- **Parallel & Distributed Execution:** Some parts of a pipeline can be parallelized or distributed across multiple compute resources, improving performance and scalability.
````

## File: content/core-concepts/ontologies.mdx
````
---
title: Ontologies
---

export function generateMetadata() {
  return {
    title: "Cognee - Ontologies",
    description: "Cognee supports rdf/xml ontologies to ground the knowledge base with general information about individuals and classes.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/core-concepts/ontologies",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/core-concepts/ontologies",
      type: "website",
      title: "Cognee - Ontologies",
      description: "Cognee supports rdf/xml ontologies to ground the knowledge base with general information about individuals and classes.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee - Ontologies",
      description: "Cognee supports rdf/xml ontologies to ground the knowledge base with general information about individuals and classes.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


# Ontology concept

Cognee optionally uses rdf/xml ontologies to ground the knowledge base with general information about individuals and classes. In order to add your own ontologies you can provide it as a parameter to the main [cognify](https://github.com/topoteretes/cognee/blob/main/cognee/api/v1/cognify/cognify_v2.py) pipeline in the following way:



```python

pipeline_run = await cognee.cognify(ontology_file_path='YOUR_ONTOLOGY_PATH')

```



### Parameters

- `datasets: Union[str, list[str]] = None`: A string or list of dataset names to be processed.

- `user: User = None`: The user requesting the processing. If not provided, the default user is retrieved.

- `ontology_file_path: Optional = None`: File path of the rdf/xml ontology file. If not provided, the default ontology is an empty ontology


### Ontology matching algorithm logic

#### Entity Extraction:
The main Cognee pipeline first extracts entities, their types, and connections from the textual input.
#### Subgraph Matching:
The system compares and matches nodes from the ontology to the extracted entities or entity types based on node similarity.
#### Mapping Entities and Classes:
#### Mapping Entities and Classes:
Entities are linked to specific individuals in the ontology.
Entity types are associated with corresponding ontology classes.
#### Knowledge Graph Enrichment:
Once a match is identified, Cognee retrieves the relevant subgraph from the ontology and merges its nodes and edges into the knowledge graph.
This process enhances the knowledge graph with a semantically rich, ontology-grounded structure.
````

## File: content/core-concepts/pipelines.mdx
````
---
title: Pipelines
---

export function generateMetadata() {
  return {
    title: "Cognee - Pipelines",
    description: "Cognee uses pipelines and tasks to analyze and enrich data, enhancing the quality of answers produced by Large Language Models (LLMs).",
    alternates: {
      canonical: "https://www.docs.cognee.ai/core-concepts/pipelines",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/core-concepts/pipelines",
      type: "website",
      title: "Cognee - Pipelines",
      description: "Cognee uses pipelines and tasks to analyze and enrich data, enhancing the quality of answers produced by Large Language Models (LLMs).",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee - Pipelines",
      description: "Cognee uses pipelines and tasks to analyze and enrich data, enhancing the quality of answers produced by Large Language Models (LLMs).",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


# PIPELINES
Cognee uses [tasks](https://github.com/topoteretes/cognee/blob/main/cognee/modules/pipelines/tasks/Task.py) grouped into pipelines that populate graph and vector stores. [These tasks](https://github.com/topoteretes/cognee/tree/main/cognee/tasks) analyze and enrich data, enhancing the quality of answers produced by Large Language Models (LLMs).

The tasks are managed and executed asynchronously using the `run_tasks` and `run_tasks_parallel` functions.

```python
pipeline = run_tasks(tasks, documents)

async for result in pipeline:
    print(result)
```

## Main pipeline: [cognee.cognify](https://github.com/topoteretes/cognee/blob/168cb5d1bf1964b5b0c645b2f3d8638d84554fda/cognee/api/v1/cognify/cognify_v2.py#L38)

This is the main pipeline currently implemented in cognee. It is designed to process data in a structured way and populate the graph and vector stores.

This function is the entry point for processing datasets. It handles dataset retrieval, user authorization, and manages the execution of a pipeline of tasks that process documents.

### Parameters

- `datasets: Union[str, list[str]] = None`: A string or list of dataset names to be processed.

- `user: User = None`: The user requesting the processing. If not provided, the default user is retrieved.

### Steps in the Function

#### User Authentication

```python
if user is None:
    user = await get_default_user()
```

If no user is provided, the function retrieves the default user.

#### Handling Empty or String Dataset Input

```python
existing_datasets = await get_datasets(user.id)

if datasets is None or len(datasets) == 0:
        datasets = existing_datasets
if type(datasets[0]) == str:
        datasets = await get_datasets_by_name(datasets, user.id)
```

If no datasets are provided, the function retrieves all datasets owned by the user. If a list of dataset names (strings) is provided, they are converted into dataset objects.

#### Selecting datasets from the input list that are owned by the user

```python
existing_datasets_map = {
        generate_dataset_name(dataset.name): True for dataset in existing_datasets
    }
```

#### Run Cognify Pipeline for Each Dataset

```python
awaitables = []

for dataset in datasets:
    dataset_name = generate_dataset_name(dataset.name)
    if dataset_name in existing_datasets_map:
        awaitables.append(run_cognify_pipeline(dataset, user))
        
return await asyncio.gather(*awaitables)
```
The `run_cognify_pipeline` function is defined within `cognify` and is responsible for processing a single dataset. This is where most of the heavy lifting occurs. The function processes multiple datasets concurrently using `asyncio.gather`.

#### Pipeline Tasks

The pipeline consists of several tasks, each responsible for different parts of the processing:

- `classify_documents`: Converts each of the documents into one of the specific Document types: PdfDocument, AudioDocument, ImageDocument or TextDocument

- `check_permissions_on_documents`: Checks if the user has the necessary permissions to access the documents. In this case, it checks for "write" permission.

- `extract_chunks_from_documents`: Extracts text chunks based on the document type.

- `add_data_points`: Creates nodes and edges from the chunks and their properties. Adds them to the graph engine.

- `extract_graph_from_data`: Generates knowledge graphs from the document chunks.

- `summarize_text`: Extracts a summary for each chunk using an llm.

![cognify pipeline](/images/cognify_pipeline.png)
````

## File: content/how-to-guides/deployment/_meta.js
````javascript
const meta = {
  mcp: "MCP",
  modal: "Modal",
  helm: "Helm",
}

export default meta;
````

## File: content/how-to-guides/deployment/helm.mdx
````
---
title: Helm
---

export function generateMetadata() {
  return {
    asIndexPage: true,
    title: "Cognee Deployment - Helm",
    description: "Learn how to deploy cognee on Kubernetes using Helm chart.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/how-to-guides/deployment/helm",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/how-to-guides/deployment/helm",
      type: "website",
      title: "Cognee Deployment - Helm",
      description: "Learn how to deploy cognee on Kubernetes using Helm chart.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Deployment - Helm",
      description: "Learn how to deploy cognee on Kubernetes using Helm chart.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


# Deploying cognee with Helm

cognee can be deployed on Kubernetes using our Helm chart, which provides a comprehensive infrastructure setup.

#### Let's deploy cognee on Kubernetes

<details>
  <summary>Step 1: Install Prerequisites</summary>
  
  Before deploying, ensure you have:
  - A running Kubernetes cluster (e.g., Minikube, GKE, EKS)
  - [Helm](https://helm.sh/docs/intro/install/) installed and configured
  - [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) installed and configured
</details>

<details>
  <summary>Step 2: Clone the Repository</summary>
  ```bash
  git clone https://github.com/topoteretes/cognee.git
  ```
</details>

<details>
  <summary>Step 3: Deploy Helm Chart</summary>
  ```bash
  helm install cognee ./cognee-chart
  ```
  
  To uninstall the release:
  ```bash
  helm uninstall cognee
  ```
</details>

--------------------------

#### Join the Conversation!
Have questions about Kubernetes deployment? Join our community to connect with professionals, share insights, and get your questions answered!
<br></br>
  <a href="https://discord.gg/m63hxKsp4p" target="_blank" rel="noopener noreferrer">
    <button className="button cta-button">
      Join the community
    </button>
  </a>
````

## File: content/how-to-guides/deployment/mcp.mdx
````
---
title: MCP
---

export function generateMetadata() {
  return {
    asIndexPage: true,
    title: "Cognee Deployment - MCP",
    description: "Learn how to run cognee MCP server.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/how-to-guides/deployment/mcp",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/how-to-guides/deployment/mcp",
      type: "website",
      title: "Cognee Deployment - MCP",
      description: "Learn how to run cognee MCP server.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Deployment - MCP",
      description: "Learn how to run cognee MCP server.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}

# Deploying cognee MCP Server

The cognee MCP (Model Context Protocol) server is a standalone component that can be deployed locally or in your infrastructure.

#### Manual Installation Steps

<details>
  <summary>Step 1: Clone the Repository</summary>
  ```bash
  git clone https://github.com/topoteretes/cognee.git
  ```
</details>

<details>
  <summary>Step 2: Install Dependencies</summary>
  First install uv package manager:
  ```bash
  brew install uv
  ```
  
  Then install project dependencies:
  ```bash
  cd cognee-mcp
  uv sync --dev --all-extras --reinstall
  ```
</details>

<details>
  <summary>Step 3: Activate Virtual Environment</summary>
  ```bash
  source .venv/bin/activate
  ```
</details>

--------------------------

#### Need Help?
Have questions about MCP server deployment? Join our community to connect with professionals, share insights, and get your questions answered!
<br></br>
  <a href="https://discord.gg/m63hxKsp4p" target="_blank" rel="noopener noreferrer">
    <button className="button cta-button">
      Join the community
    </button>
  </a>
````

## File: content/how-to-guides/deployment/modal.mdx
````
---
title: Modal
---

export function generateMetadata() {
  return {
    asIndexPage: true,
    title: "Cognee Deployment - Modal",
    description: "Learn how to run distributed cognee pipelines using Modal.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/how-to-guides/deployment/modal",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/how-to-guides/deployment/modal",
      type: "website",
      title: "Cognee Deployment - Modal",
      description: "Learn how to run distributed cognee pipelines using Modal.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Deployment - Modal",
      description: "Learn how to run distributed cognee pipelines using Modal.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


# Deploying cognee 


cognee is a standalone tool that can be deployed easily on-prem or in the cloud
It comes with a docker image and the library can be run as a pod with connections to the external Postgres database, vector, and graph stores

#### Let's deploy cognee on Modal

Modal is a cloud-function platform that lets you run any code remotely within seconds.

<details>
  <summary>Step 1: Create Modal account</summary>
  
  If you haven't used Modal yet, just go to their [website](https://modal.com/) and create an account.  
</details>
<details>
  <summary>Step 2: Clone cognee repo</summary>
  ```
    git clone https://github.com/topoteretes/cognee.git
  ```
</details>
<details>
  <summary>Step 3: Install with poetry</summary>
  
  Navigate to cognee repo
  ``` 
  cd cognee
  ```
  Install with poetry
  ``` 
  poetry install 
  ```
</details>
<details>
  <summary>Step 4: Run modal example</summary>
  The file modal_deployment in the cognee repo contains a set of statements that will be turned into semantic memory by launching a set of modal containers that process and turn the data into graph/vector representation.
  
  Run 
  ``` 
  modal run -d modal_deployment.py
  ```
  Now navigate to your modal account to see your jobs and results
</details>



--------------------------


<iframe 
  width="600" 
  height="340" 
  src="https://www.youtube.com/embed/86SWVdI5K0Y" 
  title="cognee modal deployment" 
  frameBorder="0" 
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
  allowFullScreen
></iframe>

If you need help with deploying cognee, we have the following:
1. Helm charts for k8 deployment
2. AWS Lambda or Google Cloud deployments


#### Join the Conversation!
Have questions? Join our community now to connect with professionals, share insights, and get your questions answered!
<br></br>
  <a href="https://discord.gg/m63hxKsp4p" target="_blank" rel="noopener noreferrer">
    <button className="button cta-button">
      Join the community
    </button>
  </a>
````

## File: content/how-to-guides/optimization/_meta.js
````javascript
const meta = {
  "descriptive-metrics": "Descriptive Metrics",
  "evaluation-framework": "Evaluation Framework",
};

export default meta;
````

## File: content/how-to-guides/optimization/descriptive-metrics.mdx
````
---
title: Descriptive Metrics for Graph Validation
---

export function generateMetadata() {
  return {
    title: "Cognee - Descriptive Metrics for Graph Validation",
    description: "Cognee provides key insights into the correctness and structure of the generated knowledge graph.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/how-to-guides/optimization/descriptive-metrics",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/how-to-guides/optimization/descriptive-metrics",
      type: "website",
      title: "Cognee - Descriptive Metrics for Graph Validation",
      description: "Cognee provides key insights into the correctness and structure of the generated knowledge graph.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee - Descriptive Metrics for Graph Validation",
      description: "Cognee provides key insights into the correctness and structure of the generated knowledge graph.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}

# Descriptive Metrics for Graph Validation

The [**descriptive metrics**](https://github.com/topoteretes/cognee/blob/dev/cognee/modules/data/operations/get_pipeline_run_metrics.py) functionality in Cognee provides key insights into the correctness and structure of the generated knowledge graph. 
These metrics help ensure the integrity of the graph, detect inconsistencies, and evaluate the efficiency of the Cognee pipeline.

Here's how to generate descriptive metrics in Cognee:
<details>
  <summary>Step 1: Prepare your documents</summary>
  <p>&nbsp;</p>
  
  For this example, let's use a short text.
   ```python
    text = """
    Natural language processing (NLP) is an interdisciplinary
    subfield of computer science and information retrieval.
    """
    ```
</details>

<details>
  <summary>Step 2: Prune, Add, Cognify!</summary>
  <p>&nbsp;</p>

  Before processing new data, clear any previously stored information.   
  ```python
    await cognee.prune.prune_data()
    await cognee.prune.prune_system(metadata=True)
  ```

  Add the documents (in this case, a single string) to Cognee.
  ```python
    await cognee.add(text)
  ```

  Cognify! (Knowledge graph generation step)
  - This step extracts insights, generates summaries, and creates connections.
  - During this process, descriptive metrics are calculated in the background.
  ```python
    pipeline_run = await cognee.cognify()
  ```
</details>

<details>
  <summary>Step 3: Calculate and save descriptive metrics</summary>
  <p>&nbsp;</p>

  This step saves descriptive metrics to the database. Resource-intensive calculations can be turned off using the include_optional parameter.

  ```python
    await cognee.get_pipeline_run_metrics(pipeline_run, include_optional=True)
  ```
</details>

<details>
  <summary>Step 4: Retrieve descriptive metrics from the database</summary>

  - Open PG Admin (or your database management tool) and refresh the database.
  <img src="/images/pgadmin_refresh.png" alt="Refresh database" width="250">
  </img>
  - Find the graph_metrics table and retrieve the computed metrics.
  <img src="/images/pgadmin_graphmetrics.png" alt="Metrics in pgadmin">
  </img>

  > Note: postgres and pgvector needs to be set in the env variables 
  >
</details>

For interpreting graph metrics, see our [Descriptive Metrics](/reference/descriptive-metrics) reference.

#### Join the Conversation!
Join our community now to connect with professionals, share insights, and get your questions answered!
<br></br>
  <a href="https://discord.gg/m63hxKsp4p" target="_blank" rel="noopener noreferrer">
    <button className="button cta-button">
      Join the community
    </button>
  </a>
````

## File: content/how-to-guides/optimization/evaluation-framework.mdx
````
---
title: Evaluation Framework
---

export function generateMetadata() {
  return {
    title: "Cognee - Evaluation Framework",
    description: "Cognee's evaluation framework. Configure and run evaluations in cognee. Capture specific metrics, iterate on your pipeline with confidence.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/how-to-guides/optimization/evaluation-framework",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/how-to-guides/optimization/evaluation-framework",
      type: "website",
      title: "Cognee - Evaluation Framework",
      description: "Cognee's evaluation framework. Configure and run evaluations in cognee. Capture specific metrics, iterate on your pipeline with confidence.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee - Evaluation Framework",
      description: "Cognee's evaluation framework. Configure and run evaluations in cognee. Capture specific metrics, iterate on your pipeline with confidence.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}

# Cognee Evaluation Framework

Without evaluation, you have no objective way to know if your system's answers are good or bad. With cognee's evaluation framework, you will easily configure and run evaluations in cognee using the `run_eval.py` entry point. By capturing specific metrics, you can iterate on your pipeline with confidence. Below, you will find how to:

1. Build or reuse an existing corpus.
2. Generate and retrieve answers.
3. Evaluate the answers using different metrics.
4. Visualize the metrics in a dashboard.

#### To run evaluations quickly with cognee:

<details>
  <summary>Step 1: Clone cognee repo</summary>
  ```
    git clone https://github.com/topoteretes/cognee.git
  ```
</details>
<details>
  <summary>Step 2: Install with poetry</summary>

  Navigate to cognee repo
  ```
  cd cognee
  ```
  Install with poetry
  ```
  poetry install
  ```
</details>
<details>
  <summary>Step 3: Run evaluation for a dummy question</summary>

  Run
  ```
  python evals/eval_framework/run_eval.py
  ```
</details>
<details>
  <summary>Step 4: Navigate to the output files to see the results</summary>
  - "questions_output.json"
  - "answers_output.json"
  - "metrics_output.json"
  - "dashboard.html"

  Explore the details and further explanation below.

</details>

Here is a high-level diagram of the evaluation process, illustrating how various executors interact:

<img src="/images/cognee_evaluation_diagram.png" alt="cognee_evaluation_diagram" width="900"/>

## Let's explore each executor and learn how to configure them

<details>
  <summary>Preliminaries: Configuration with eval_config.py</summary>

  All the parameters mentioned throughout this documentation are defined in the `eval_config.py` file. This configuration file uses Pydantic settings to manage all evaluation parameters in one place.

  ```python
  # Example from eval_config.py
  class EvalConfig(BaseSettings):
      # Corpus builder params
      building_corpus_from_scratch: bool = True
      number_of_samples_in_corpus: int = 1
      benchmark: str = "Dummy"
      # ... more parameters
  ```

  You can override any of these parameters by setting them in your `.env` file. For example:

  ```
  # .env file example
  BUILDING_CORPUS_FROM_SCRATCH=False
  NUMBER_OF_SAMPLES_IN_CORPUS=10
  BENCHMARK=HotPotQA
  DEEPEVAL_MODEL=gpt-4o
  ```

  This makes it easy to customize your evaluation runs without modifying the code. All the parameters described in the following sections can be configured this way.
</details>

### 1. Main (run_eval) & cognee Framework
- Main (run_eval) orchestrates the entire flow.
- cognee Framework provides the underlying infrastructure to run cognee's cognify pipeline.

Here's what happens step-by-step when you run the evaluation:

- **Configuration Loading**: The script first loads all parameters from `eval_config.py`, which can be overridden by your `.env` file.
- **Corpus Building**: Calls `run_corpus_builder()` to either create a new corpus or use an existing one.
- **Question Answering**: Executes `run_question_answering()` to generate answers for each question in the corpus.
- **Evaluation**: Runs `run_evaluation()` to calculate metrics comparing generated answers with reference answers.
- **Dashboard Generation**: If enabled, creates a visual dashboard using `create_dashboard()` to help you analyze the results.

Each step produces output files that feed into the next step, creating a complete evaluation pipeline.

### 2. Corpus Building
A corpus is a collection of questions and contexts that the system will cognify and use to generate question answers which will later be evaluated. The `CorpusBuilderExecutor` is responsible for loading questions and contexts from one of the supported benchmarks, then "cognifying" them (processing and storing them in cognee's system).

#### Benchmark Adapters
Cognee supports multiple benchmark datasets through adapter classes:

- **BaseBenchmarkAdapter**: An abstract base class that defines the interface for all benchmark adapters.
- **Implementations**:
  - **HotpotQAAdapter**: Loads multi-hop questions from the HotpotQA dataset.
  - **TwoWikiMultihopAdapter**: Extends HotpotQA with additional evidence from the 2WikiMultihop dataset.
  - **MusiqueAdapter**: Handles the Musique dataset with question decomposition.
  - **DummyAdapter**: Provides a simple test question for quick demonstrations.

Each adapter loads questions, their answers, and context documents. The golden answers are saved for later evaluation but aren't cognified. Optionally, adapters can also extract "golden contexts" (the specific parts of documents that answer the question) for context evaluation.

#### Task Getters
The `task_getter` parameter allows flexibility in how cognee processes the corpus:

- It determines which pipeline will be used to process the documents.
- By default, it uses the standard cognee pipeline, but you can configure alternative pipelines.
- This is useful for comparing different processing strategies in your evaluations.

#### Configuring Corpus Building

```python
building_corpus_from_scratch: bool = True
number_of_samples_in_corpus: int = 1
benchmark: str = "Dummy"  # Options: 'HotPotQA', 'TwoWikiMultiHop', 'Musique', 'Dummy'
task_getter_type: str = "Default"  # Options: 'Default', 'CascadeGraph'
```

- **building_corpus_from_scratch**: `True` for building a fresh corpus and removing existing data, while `False` indicates that it will not rebuild the corpus (and will not delete any existing data).
- **number_of_samples_in_corpus**: How many questions you want to include from the selected benchmark.
- **benchmark**: The dataset or benchmark from which questions are sampled.
- **task_getter_type**: Determines which pipeline configuration to use when processing documents.

#### Implementation Details

The corpus building process is implemented in several key files:

- **run_corpus_builder.py**: This is the entry point called by `run_eval.py`. It:
  - Creates a `CorpusBuilderExecutor` with the specified benchmark and task getter
  - Calls the executor to build the corpus with the configured parameters
  - Saves the questions to the output file and the relational database
  - Handles the `evaluating_contexts` flag to determine whether to load golden contexts

- **corpus_builder_executor.py**: Contains the core logic for building the corpus:
  - Defines the `CorpusBuilderExecutor` class that orchestrates the corpus building process
  - Loads the appropriate benchmark adapter based on the configuration
  - Calls cognee's core functions to process and store the documents
  - Manages the execution of the configured task getter pipeline

- **base_benchmark_adapter.py**: Defines the abstract interface that all benchmark adapters must implement:
  - Provides a consistent `load_corpus` method that all adapters must implement
  - Ensures all adapters can handle parameters like sample limits and golden context loading

These files work together to load questions and contexts from the selected benchmark, process them through cognee's pipeline, and prepare them for the question answering phase.

### 3. Question Answering
This is where cognee retrieves relevant context and generates answers to the questions. The `AnswerGeneratorExecutor` processes each question from the corpus built in the previous step.

Here's what happens step-by-step:

1. **Load Questions**: The executor reads questions from the `questions_output.json` file created in the corpus building step.
2. **Context Retrieval**: For each question, the system retrieves relevant context using the configured retriever.
3. **Answer Generation**: Using the retrieved context, the system generates an answer to the question.
4. **Save Results**: The questions, generated answers, golden answers, and optionally the retrieval contexts are saved to `answers_output.json`.

#### Available Retrievers
Cognee supports multiple retrieval strategies through different retriever classes:

- **CompletionRetriever** (`cognee_completion`): The standard retriever that uses semantic search to find relevant context.
- **GraphCompletionRetriever** (`cognee_graph_completion`): Uses graph-based retrieval to find connected information across documents.
- **GraphSummaryCompletionRetriever** (`graph_summary_completion`): Combines graph retrieval with summarization for more concise context.

Each retriever has different strengths depending on the types of questions and data you're working with.

#### Configuring Question Answering

```python
answering_questions: bool = True
qa_engine: str = "cognee_completion"  # Options: 'cognee_completion', 'cognee_graph_completion', 'graph_summary_completion'
evaluating_contexts: bool = True  # Controls whether contexts are saved for evaluation
```

- **answering_questions**: `True` means the `AnswerGeneratorExecutor` will retrieve context and generate answers. `False` for skipping the answer generation step (e.g., if you just want to rebuild a corpus).
- **qa_engine**: Specifies the retriever used for finding context and generating answers.
- **evaluating_contexts**: When `True`, the system will save both the retrieved contexts and the golden contexts (if available) for evaluation. This allows you to assess not just answer quality but also retrieval quality.

The retrieved contexts are saved alongside the answers and can be evaluated in the next phase of the pipeline to assess the quality of the retrieval process.

#### Implementation Details

The question answering process is implemented in two main files:

- **run_question_answering_module.py**: This is the entry point called by `run_eval.py`. It:
  - Loads questions from the output file of the corpus building step
  - Instantiates the appropriate retriever based on the `qa_engine` parameter
  - Calls the `AnswerGeneratorExecutor` to process each question
  - Saves the results to the answers output file and the relational database

- **answer_generation_executor.py**: Contains the core logic for answering questions:
  - Defines the `AnswerGeneratorExecutor` class with the `question_answering_non_parallel` method
  - Maps retriever names to their implementation classes via the `retriever_options` dictionary
  - For each question, retrieves context and generates an answer using the configured retriever
  - Packages the question, answer, golden answer, and retrieval context into a structured format

These files work together to transform the questions from the corpus into answered questions with their associated contexts, ready for evaluation.

### 4. Evaluating the Answers
After the questions are answered, cognee evaluates each answer against benchmark's reference ("golden") answer using specified metrics. This lets you see how reliable or accurate your system is.

Here's what happens step-by-step:

1. **Load Answers**: The executor reads answers from the `answers_output.json` file created in the question answering step.
2. **Initialize Evaluator**: The system creates an evaluator based on the configured evaluation engine.
3. **Apply Metrics**: For each answer, the system calculates scores using the specified metrics.
4. **Save Results**: The evaluation results are saved to `metrics_output.json` and the relational database.

#### Available Evaluators
Cognee supports multiple evaluation approaches through different adapter classes:

- **DeepEvalAdapter**: Uses the DeepEval library to calculate metrics, supporting both traditional metrics and LLM-based evaluations.
- **DirectLLMEvalAdapter**: Uses a direct call to an LLM with custom prompts to evaluate answer correctness.

#### Evaluation Metrics
Depending on the evaluator, different metrics are available:

- **correctness**: Uses an LLM-based approach to see if the meaning of the answer aligns with the golden answer.
- **EM** (Exact Match): Checks if the generated answer exactly matches the golden answer.
- **f1**: Uses token-level matching to measure precision and recall.
- **contextual_relevancy**: Evaluates how relevant the retrieved context is to the question (when context evaluation is enabled).
- **context_coverage**: Assesses how well the retrieved context covers the information needed to answer the question (when context evaluation is enabled).

#### Configuring Evaluation

```python
evaluating_answers: bool = True
evaluating_contexts: bool = True
evaluation_engine: str = "DeepEval"  # Options: 'DeepEval', 'DirectLLM'
evaluation_metrics: List[str] = ["correctness", "EM", "f1"]
deepeval_model: str = "gpt-4o-mini"
```

- **evaluating_answers**: `True` triggers the `EvaluationExecutor` to evaluate the answers.
- **evaluating_contexts**: When `True`, additional context-related metrics are included in the evaluation.
- **evaluation_engine**: The evaluation adapter to use.
- **evaluation_metrics**: The list of metrics to calculate for each answer.
- **deepeval_model**: The LLM used for computing the LLM-based metrics (e.g., `gpt-4o-mini`).

#### Implementation Details

The evaluation process is implemented in several key files:

- **run_evaluation_module.py**: This is the entry point called by `run_eval.py`. It:
  - Loads answers from the output file of the question answering step
  - Initializes the appropriate evaluator based on the `evaluation_engine` parameter
  - Calls the `EvaluationExecutor` to process each answer
  - Saves the results to the metrics output file and the relational database

- **evaluation_executor.py**: Contains the core logic for evaluating answers:
  - Defines the `EvaluationExecutor` class that orchestrates the evaluation process
  - Selects the appropriate evaluator adapter based on configuration
  - Adds context evaluation metrics if context evaluation is enabled

- **evaluator_adapters.py**: Defines the available evaluator adapters:
  - Maps evaluator names to their implementation classes
  - Provides a consistent interface for different evaluation approaches

- **deep_eval_adapter.py** and **direct_llm_eval_adapter.py**: Implement specific evaluation strategies:
  - DeepEvalAdapter uses the DeepEval library with multiple metrics
  - DirectLLMAdapter uses direct LLM calls with custom prompts

These files work together to evaluate the quality of the generated answers and optionally the retrieved contexts.

### 5. Creating Dashboard
Cognee generates a visual dashboard to help you analyze evaluation results. The dashboard presents metrics in an interactive HTML file that you can open in any web browser, making it easy to spot patterns and issues in your model's outputs.

Here's what happens step-by-step:

1. **Load Metrics**: The dashboard generator reads metrics from the `metrics_output.json` and `aggregate_metrics.json` files.
2. **Generate Visualizations**: The system creates various charts and tables to visualize the evaluation results.
3. **Compile HTML**: All visualizations are combined into a single HTML file with CSS styling and JavaScript for interactivity.
4. **Save Dashboard**: The complete dashboard is saved to `dashboard.html` for easy viewing.

#### Dashboard Features
The generated dashboard includes several key visualizations:

- **Distribution Histograms**: Shows the distribution of scores for each metric, helping you understand the overall performance patterns.
- **Confidence Interval Plot**: Displays the mean score and 95% confidence interval for each metric, giving you statistical insight into the reliability of the results.
- **Detailed Tables**: For each metric, a table shows the individual scores, reasons, and relevant data (questions, answers, contexts) for in-depth analysis.

#### Configuring Dashboard Generation

```python
dashboard: bool = True
aggregate_metrics_path: str = "aggregate_metrics.json"
dashboard_path: str = "dashboard.html"
```

- **dashboard**: When `True`, the system will generate the dashboard visualization.
- **aggregate_metrics_path**: The path where aggregate metrics (means, confidence intervals) are stored.
- **dashboard_path**: The output path for the generated HTML dashboard.

#### Implementation Details

The dashboard generation is implemented in the `metrics_dashboard.py` file, which contains several key functions:

- **create_dashboard()**: The main entry point that orchestrates the dashboard creation process:
  - Reads metrics data from the output files
  - Calls visualization functions to generate charts
  - Assembles the complete HTML dashboard
  - Saves the result to the specified output file

- **create_distribution_plots()**: Generates histograms showing the distribution of scores for each metric.

- **create_ci_plot()**: Creates a bar chart with error bars showing the mean and confidence interval for each metric.

- **generate_details_html()**: Produces HTML tables with detailed information about each evaluation result.

- **get_dashboard_html_template()**: Assembles all visualizations into a complete HTML document with styling.

This dashboard provides a comprehensive view of your evaluation results, making it easy to understand how well your system is performing and where improvements might be needed.

### Output Files: Where to Look

By default, the evaluation flow generates the following files (and a relational database) that capture the entire workflow:

```python
questions_path: str = "questions_output.json"
answers_path: str = "answers_output.json"
metrics_path: str = "metrics_output.json"
dashboard_path: str = "dashboard.html"
```

<details>
  <summary>questions_output.json</summary>
    Contains the question objects produced by the corpus builder. Example:
    ```json
        [
          {
            "answer": "Yes",
            "question": "Is Neo4j supported by cognee?",
            "type": "dummy"
          }
        ]
    ```
</details>
<details>
  <summary>answers_output.json</summary>
    Contains the generated answers, alongside their original questions and reference ("golden") answers. Example:
    ```json
    [
      {
        "question": "Is Neo4j supported by cognee?",
        "answer": "Yes, Neo4j is supported by cognee.",
        "golden_answer": "Yes"
      }
    ]
    ```
</details>
<details>
  <summary>metrics_output.json</summary>
    Contains evaluation results for each question, including scores and rationales. All the prompts that cognee is using right now is to maximize user experience and not the scores. So cognee provides a broader answer to the user as base setting. Example: 
    ```json
    [
      {
        "question": "Is Neo4j supported by cognee?",
        "answer": "Yes, Neo4j is supported by cognee.",
        "golden_answer": "Yes",
        "metrics": {
          "correctness": {
            "score": 0.7815554704711645,
            "reason": "The actual output confirms that Neo4j is supported by cognee, which aligns with the expected output's affirmative response, but it contains unnecessary detail..."
          },
          "EM": {
            "score": 0.0,
            "reason": "Not an exact match"
          },
          "f1": {
            "score": 0.2857142857142857,
            "reason": "F1: 0.29 (Precision: 0.17, Recall: 1.00)"
          }
        }
      }
    ]
    ```
</details>
<details>
  <summary>dashboard.html</summary>
    A HTML dashboard that summarizes all the metrics visually. You can find an example [here](/dashboard.html).  
    <iframe
      src="/dashboard.html"
      width="800"
      height="400"
      style={{ border: '1px solid #ccc' }}
      title="Dashboard">
    </iframe>
</details>    

---

## Are you ready to test it out with your parameters? 

Configure the above parameters as you wish in your .env file and simply run:
```
python evals/eval_framework/run_eval.py
```

Using cognee's evaluation framework, you can:
  1. Build (or reuse) a corpus from the specified benchmark.
  2. Generate answers to the collected questions.
  3. Evaluate those answers using the metrics you specified.
  4. Produce a dashboard summarizing the results.
  5. Inspect the outputs.
    - **`questions_output.json`** for generated or fetched questions.
    - **`answers_output.json`** for final answers and reference answers.
    - **`metrics_output.json`** for the calculated metrics.
    - **`dashboard.html`** to visually explore the evaluation results.

Feel free to reach out with any questions or suggestions on how to improve the evaluation framework. 

---

#### Join the Conversation!
Join our community now to connect with professionals, share insights, and get your questions answered!
<br></br>
  <a href="https://discord.gg/m63hxKsp4p" target="_blank" rel="noopener noreferrer">
    <button className="button cta-button">
      Join the community
    </button>
  </a>
````

## File: content/how-to-guides/_meta.js
````javascript
const meta = {
  deployment: "Deployment",
  "graph-visualization": "Graph Visualization",
  search: "Search Guide",
  optimization: {
    type: "doc",
    title: "Optimization",
  },
  configuration: "Configuration",
  "remote-models": "Remote Models",
  "local-models": "Local Models",
  "cognee-tasks": "Cognee Tasks",
  "own-data-model": "Own Data Model",
};

export default meta;
````

## File: content/how-to-guides/cognee-tasks.mdx
````
---
title: Tasks
---

export function generateMetadata() {
  return {
    title: "Cognee - Tasks",
    description: "Cognee let's you define your own custom logic for graph enrichment and retrieval.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/how-to-guides/cognee-tasks",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/how-to-guides/cognee-tasks",
      type: "website",
      title: "Cognee - Tasks",
      description: "Cognee let's you define your own custom logic for graph enrichment and retrieval.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee - Tasks",
      description: "Cognee let's you define your own custom logic for graph enrichment and retrieval.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


# How to customize cognee and add your logic

**Difficulty**: Medium

## Overview

Cognee let's you define your own custom logic for graph enrichment and retrieval.

#### Let's create custom cognee tasks

Adding data to our graph and connecting it to LLM can help LLM reason better
You move from large amounts to text to structured data. See before and after bellow

Here is what we start with:

![Before ](/images/cognee_raw_text_example.png)

And here is how it ends:

![After ](/images/cognee_graph_example.png)

<details>
  <summary>Step 1: Clone cognee repo</summary>
      ```
    git clone https://github.com/topoteretes/cognee.git
    ```


</details>
<details>
  <summary>Step 2: Install with poetry</summary>

  Navigate to cognee repo
  ```
  cd cognee
  ```
  Install with poetry
  ```
  poetry install
  ```
</details>
<details>
  <summary>Step 3: Run simple cognee script relational data</summary>
    Create a python file called simple_example.py
    and the code from the following link into it

    https://github.com/topoteretes/cognee-starter/blob/main/src/pipelines/low_level.py
</details>

#### Let's stop for a moment to understand what the script does?

It:
1. Reads Data from JSON Files
2. The script opens two files—companies.json and people.json—that contain information about companies, their departments, and people working in those departments.
3. Creates Connected Data Objects (DataPoints)

    “DataPoints” are just special classes (like Person, Department, Company) that Cognee uses to understand how the data is linked.
    Each object type (e.g., Person, Department, Company) defines what information it holds (like “name”) and how it relates to other objects (people belong to departments, departments belong to companies, etc.).
    Stores Everything in a Cognee Knowledge Graph

    A “knowledge graph” is like a network of information. It links all the objects together:
    Each Company node links to its departments,
    Each Department node links to its employees, and so on.
    By saving data in a graph, questions like “Who works for GreenFuture Solutions?” become easier to answer because Cognee can “walk” the connections and gather the right information.
4. Indexes and Visualizes the Graph

    After the data is loaded, the script runs a process called “indexing.” This makes it easier and faster to search relationships in the graph.
    It then creates an HTML file to show you a visual representation of the network of companies, departments, and employees.
5. Answers Questions About the Data

6. Finally, the script uses a search function to answer a query like “Who works for GreenFuture Solutions?” This works because Cognee knows about the connections in your graph.

<details>
  <summary>Step 4: Run cognee </summary>
  In order to load the data
  Run
  ```
  python simple_example.py
  ```

</details>

<details>
  <summary>Step 5: Inspect your cognee graph  </summary>
  The script will create an html file in the root folder that you can inspect and check the graph, or visualize it in the browser
      ```
import webbrowser
import os
from cognee.api.v1.visualize.visualize import visualize_graph
await visualize_graph()
home_dir = os.path.expanduser("~")
html_file = os.path.join(home_dir, "graph-visualization.html")
display(html_file)
webbrowser.open(f"file://{html_file}")
        ```
</details>


#### Join the Conversation!
Have questions? Join our community now to connect with professionals, share insights, and get your questions answered!
<br></br>
  <a href="https://discord.gg/m63hxKsp4p" target="_blank" rel="noopener noreferrer">
    <button className="button cta-button">
      Join the community
    </button>
  </a>
````

## File: content/how-to-guides/configuration.mdx
````
---
title: Configuration
---

export function generateMetadata() {
  return {
    title: "Cognee - Configuration",
    description: "Configure the vector and graph stores using the environment variables in your .env file or programmatically.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/how-to-guides/configuration",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/how-to-guides/configuration",
      type: "website",
      title: "Cognee - Configuration",
      description: "Configure the vector and graph stores using the environment variables in your .env file or programmatically.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee - Configuration",
      description: "Configure the vector and graph stores using the environment variables in your .env file or programmatically.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


# Configuration



## 🚀 Configure Vector and Graph Stores

You can configure the vector and graph stores using the environment variables in your .env file or programmatically.
We use [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#dotenv-env-support)

We have a global configuration object (cognee.config) and individual configurations on pipeline and data store levels

Check available configuration options:
``` python
from cognee.infrastructure.databases.vector import get_vectordb_config
from cognee.infrastructure.databases.graph.config import get_graph_config
from cognee.infrastructure.databases.relational import get_relational_config
from cognee.infrastructure.llm.config import get_llm_config
print(get_vectordb_config().to_dict())
print(get_graph_config().to_dict())
print(get_relational_config().to_dict())
print(get_llm_config().to_dict())
```

Setting the environment variables in your .env file, and Pydantic will pick them up:

```bash
GRAPH_DATABASE_PROVIDER = 'lancedb'
```
Otherwise, you can set the configuration yourself:

```python
cognee.config.set_llm_provider('ollama')
```

Make sure to keep your API keys secure and never commit them to version control.
````

## File: content/how-to-guides/deployment.mdx
````
---
title: Deployment
asIndexPage: true
---

export function generateMetadata() {
  return {
    title: "Cognee Deployment",
    description: "Various options to run cognee. Distributed cognee pipelines. Remote pipelines on Kubernetes.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/how-to-guides/deployment",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/how-to-guides/deployment",
      type: "website",
      title: "Cognee Deployment",
      description: "Various options to run cognee. Distributed cognee pipelines. Remote pipelines on Kubernetes.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Deployment",
      description: "Various options to run cognee. Distributed cognee pipelines. Remote pipelines on Kubernetes.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}

# Deploying cognee 

cognee is a standalone tool that can be deployed easily on-prem or in the cloud.

Try it out!
* [MCP](deployment/mcp)
* [Docker](../tutorials/use_the_api)
* [Modal](deployment/modal) for easily scalable remote
* [Helm](deployment/helm) for Kubernetes
````

## File: content/how-to-guides/graph-visualization.mdx
````
---
title: Graph Visualization
---

export function generateMetadata() {
  return {
    title: "Cognee - Graph Visualization",
    description: "Easily visialize your knowledge graph with cognee.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/how-to-guides/graph-visualization",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/how-to-guides/graph-visualization",
      type: "website",
      title: "Cognee - Graph Visualization",
      description: "Easily visialize your knowledge graph with cognee.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee - Graph Visualization",
      description: "Easily visialize your knowledge graph with cognee.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}

# Graph Visualization Guide
 
One of Cognee's most powerful features is its ability to visualize knowledge graphs. This guide explains how to generate, view, and interpret graph visualizations with default setting using NetworkX.


## Generating a Graph Visualization

<details>
  <summary>Using API (no credentials required)</summary>
    You can generate a visualization of your knowledge graph using the API:

    ```python
    import cognee
    from cognee.api.v1.visualize.visualize import visualize_graph
    import asyncio
    
    
    async def main():
        # Add some content first
        await cognee.add("Albert Einstein was a theoretical physicist born in Germany.")
        await cognee.add("Einstein developed the theory of relativity.")
    
        # Process the content
        await cognee.cognify()
    
        
        # Generate an HTML visualization of your graph
        await visualize_graph()
        
        # The file is saved in your current folder
        home_dir = os.path.expanduser("~")
        html_file = os.path.join(home_dir, "graph_visualization.html")
        display(html_file)
    

    if __name__ == "__main__":
        asyncio.run(main())
    ```
</details>

<details>
  <summary>Using Graphistry</summary>

    For this you will need to:
    - create an account and API key from https://www.graphistry.com
    - add the following environment variables to `.env` file:
    ```
    GRAPHISTRY_USERNAME=""
    GRAPHISTRY_PASSWORD=""
    ```

    ```python
    import cognee
    from cognee.shared.utils import render_graph
    import asyncio

    async def main():
        # Add some content first
        await cognee.add("Albert Einstein was a theoretical physicist born in Germany.")
        await cognee.add("Einstein developed the theory of relativity.")
        
        # Process the content
        await cognee.cognify()
        
        # Generate the visualization
        await render_graph()
        
        # You will get the URL to graphistry something like:
        # https://hub.graphistry.com/graph/...

    if __name__ == "__main__":
        asyncio.run(main())
    ```
</details>

## Understanding the Visualization

The graph visualization shows:

### Nodes

Nodes represent entities extracted from your content:

- **People**: Individuals mentioned in your content (e.g., "Albert Einstein")
- **Concepts**: Abstract ideas or topics (e.g., "Theory of Relativity")
- **Organizations**: Companies, institutions, etc.
- **Locations**: Places mentioned in your content
- **Events**: Occurrences or happenings
- **Other entities**: Various other types of information

### Edges

Edges (lines connecting nodes) represent relationships between entities:

- The label on each edge describes the relationship (e.g., "developed", "was born in")
- The direction of the relationship is indicated by the arrow

### Interacting with the Visualization

The visualization is interactive:

- **Zoom**: Use the mouse wheel to zoom in and out
- **Pan**: Click and drag to move around the graph
- **Select**: Click on nodes to highlight their connections
- **Hover**: Hover over nodes and edges to see more details
- **Rearrange**: Drag nodes to rearrange the layout

## Example Interpretation

Let's interpret a simple example:

1. You add content about Albert Einstein
2. The visualization shows:
   - A node for "Albert Einstein" (Person)
   - A node for "Germany" (Location)
   - A node for "Theory of Relativity" (Concept)
   - An edge from Einstein to Germany labeled "was born in"
   - An edge from Einstein to Theory of Relativity labeled "developed"

This visualization helps you understand how different pieces of information are connected in your knowledge graph.


## Troubleshooting

If you're having trouble with the visualization:

1. **Empty graph**: Make sure you've added content and run `cognee.cognify()` before generating the visualization
2. **File not found**: Check the system folder path and ensure the file exists
3. **Browser security**: Some browsers restrict opening local files; try using Firefox or Chrome
4. **Large graphs**: For very large graphs, the visualization may be slow; try filtering to include only specific node types

## Next Steps

- Learn how to [query your knowledge graph](../reference/api-reference#search-and-query)
- Explore [advanced visualization options](../reference/sdk_reference)
- See how to [build custom pipelines](../core-concepts/pipelines) for specialized graph generation
````

## File: content/how-to-guides/local-models.mdx
````
---
title: Local Models
---

export function generateMetadata() {
  return {
    title: "Cognee - Local Models",
    description: "Run cognee with local models. Run cognee with Ollama. Run cognee with DeepSeek models. Run cognee with Mistral.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/how-to-guides/local-models",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/how-to-guides/local-models",
      type: "website",
      title: "Cognee - Local Models",
      description: "Run cognee with local models. Run cognee with Ollama. Run cognee with DeepSeek models. Run cognee with Mistral.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee - Local Models",
      description: "Run cognee with local models. Run cognee with Ollama. Run cognee with DeepSeek models. Run cognee with Mistral.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


## 🚀 Getting Started with Local Models

You'll need to run the local model on your machine or use one of the providers hosting the model.

We had some success with `llama3.3` and `deepseek`, but `7b` models did not work well. We recommend using `llama3.3 70b-instruct-q3_K_M` and `deepseek-r1:32b` via Ollama.

### Ollama 

Set up Ollama by following instructions on [Ollama website](https://ollama.com/)

For a quickstart simply run the model:

```bash
ollama run deepseek-r1:32b
```
and

```bash
ollama run avr/sfr-embedding-mistral:latest
```
Set the environment variable in your .env to use the model

```bash
LLM_PROVIDER = 'ollama'

```
Otherwise, you can set the configuration for the model:

```bash
cognee.config.llm_provider = 'ollama'

```
You can also set the HOST and model name:

```bash

cognee.config.llm_endpoint = "http://localhost:11434"
cognee.config.llm_model = "ollama/llama3.2"
cognee.embedding_provider = "ollama"
cognee.embedding_model = "avr/sfr-embedding-mistral:latest"
cognee.embedding_dimensions = 4096
cognee.huggingface_tokenizer ="Salesforce/SFR-Embedding-Mistral"
```
or set the env variables in your .env file
```
EMBEDDING_PROVIDER="ollama"
EMBEDDING_MODEL="avr/sfr-embedding-mistral:latest"
EMBEDDING_ENDPOINT="http://localhost:11434/api/embeddings"
EMBEDDING_DIMENSIONS=4096
HUGGINGFACE_TOKENIZER="Salesforce/SFR-Embedding-Mistral"
```
````

## File: content/how-to-guides/own-data-model.mdx
````
---
title: Own Data Model
---

export function generateMetadata() {
  return {
    title: "Cognee - Own Data Model",
    description: "Cognee let's you organize and model your user's data for LLMs to use.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/how-to-guides/own-data-model",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/how-to-guides/own-data-model",
      type: "website",
      title: "Cognee - Own Data Model",
      description: "Cognee let's you organize and model your user's data for LLMs to use.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee - Own Data Model",
      description: "Cognee let's you organize and model your user's data for LLMs to use.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


# Customize data ingestion using Pydantic

**Difficulty**: Medium


## Overview

Cognee let's you organize and model your user's data for LLMs to use.
In this way you can choose how to load only the data you need.
Let's say you need all persons mentioned in a novel.
We enable you to:
1. Specify which persons you want extracted
2. Load them into the cognee data store
3. Retrieve them with natural language query

Let's try it out!

#### Let's model your data based on your preferences


Why is this important? Let's visualize our data before and after.


On this image you can see that purple color nodes are exactly the nodes that represent people mentioned in the novel.


![After ](/images/base_person_graph.png)


Let's create the graph ourselves.



<details>
  <summary>Step 1: Clone cognee repo</summary>
    Clone main git repo
    ```
    git clone https://github.com/topoteretes/cognee.git
    ```
    And our getting started repo
        ```
    git clone https://github.com/topoteretes/cognee-starter.git
        ```

</details>

<details>
  <summary>Step 2: Install with poetry</summary>

  Navigate to cognee repo
  ```
  cd cognee
  ```
  Install with poetry
  ```
  poetry install
  ```
</details>

<details>
  <summary>Step 3: Use example from our starter repo </summary>

  Create a python script called example_ontology.py and copy the content of the following file to it

    https://github.com/topoteretes/cognee-starter/blob/main/src/pipelines/custom-model.py

</details>

<details>
  <summary>Step 4: Run the script</summary>

  Run the script using python
  ```
    python example_ontology.py
  ```
    Make sure that the script has access to the data in the cognee-starter repo
</details>

<details>
  <summary>Step 5: Inspect your graph</summary>

    The script will create an html file in the root folder that you can inspect and check the graph.
    You can also run a small http server that will render your semantic layer by doing the following
      ```
import webbrowser
import os
from cognee.api.v1.visualize.visualize import visualize_graph
await visualize_graph()
home_dir = os.path.expanduser("~")
html_file = os.path.join(home_dir, "graph-visualization.html")
webbrowser.open(f"file://{html_file}")
# display(html_file) in notebook 

        ```
</details>

#### Join the Conversation!
Have questions? Join our community now to connect with professionals, share insights, and get your questions answered!
<br></br>
  <a href="https://discord.gg/m63hxKsp4p" target="_blank" rel="noopener noreferrer">
    <button className="button cta-button">
      Join the community
    </button>
  </a>
````

## File: content/how-to-guides/remote-models.mdx
````
---
title: Remote Models
---

export function generateMetadata() {
  return {
    title: "Cognee - Remote Models",
    description: "Run cognee with custom models. Run cognee with Gemini. Run cognee with OpenRouter. Run cognee with Anyscale.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/how-to-guides/remote-models",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/how-to-guides/remote-models",
      type: "website",
      title: "Cognee - Remote Models",
      description: "Run cognee with custom models. Run cognee with Gemini. Run cognee with OpenRouter. Run cognee with Anyscale.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee - Remote Models",
      description: "Run cognee with custom models. Run cognee with Gemini. Run cognee with OpenRouter. Run cognee with Anyscale.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


## 🚀 How to Use Remote Models

First and foremost, make sure to keep your API keys secure and never commit them to version control.

### OpenAI

This is the easiest setup, technically you can start with only one set variable. If your `.env` consists only of one `LLM_API_KEY` per default it is considered as an OpenAI key.

```bash
LLM_API_KEY = "your_api_key"
```

### Google Gemini

You can use Google's Gemini models for both LLM and embeddings. Set the following environment variables in your .env file:

For embeddings:
```bash
EMBEDDING_PROVIDER="gemini"
EMBEDDING_API_KEY="your_api_key"
EMBEDDING_MODEL="gemini/text-embedding-004"
EMBEDDING_ENDPOINT="https://generativelanguage.googleapis.com/v1beta/models/text-embedding-004"
EMBEDDING_API_VERSION="v1beta"
EMBEDDING_DIMENSIONS=768
EMBEDDING_MAX_TOKENS=8076
```

For LLM:
```bash
LLM_PROVIDER="gemini"
LLM_API_KEY="your_api_key"
LLM_MODEL="gemini/gemini-1.5-flash"
LLM_ENDPOINT="https://generativelanguage.googleapis.com/"
LLM_API_VERSION="v1beta"
```

## Custom endpoints

### OpenRouter

You will need an API key set up with OpenRouter.

```
LLM_PROVIDER="custom"
LLM_API_KEY="your_api_key"
LLM_MODEL="openrouter/google/gemini-2.0-flash-lite-preview-02-05:free"
LLM_ENDPOINT="https://openrouter.ai/api/v1"
```

As of writing this OpenRouter does not have embedding models.

### Anyscale

```bash
LLM_PROVIDER = 'custom'
LLM_MODEL = "mistralai/Mixtral-8x7B-Instruct-v0.1"
LLM_ENDPOINT = "https://api.endpoints.anyscale.com/v1"
LLM_API_KEY = "your_api_key"
```
````

## File: content/how-to-guides/search.mdx
````
---
title: Search Guide
---

export function generateMetadata() {
  return {
    title: "Cognee - Search Guide",
    description: "Use cognee to retrieve data from knowledge graph. Retrieve text summaries. Retrieve knowledge graph facts.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/how-to-guides/search",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/how-to-guides/search",
      type: "website",
      title: "Cognee - Search Guide",
      description: "Use cognee to retrieve data from knowledge graph. Retrieve text summaries. Retrieve knowledge graph facts.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee - Search Guide",
      description: "Use cognee to retrieve data from knowledge graph. Retrieve text summaries. Retrieve knowledge graph facts.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}

# Search Guide

Cognee provides powerful search capabilities to query your knowledge graph. This guide explains the different search types and how to use them effectively.

> **Note:** For a comprehensive reference of all available search types, see the [Search Types Reference](../reference/search-types).

## Search Types

Cognee offers several main types of search:

### 1. Insights Search

Insights search helps you discover connections and relationships in your knowledge graph:

```python
from cognee.modules.search.types import SearchType
import cognee
import asyncio

async def main():
    results = await cognee.search(
        query_text="What is the relationship between Einstein and Germany?",
        query_type=SearchType.INSIGHTS
    )
    
    for result in results:
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

Use insights search when you want to:
- Discover relationships between entities
- Understand how concepts are connected
- Get a deeper understanding of your knowledge graph

### 2. Information Search

Information search retrieves specific facts and information from your knowledge graph:

```python
results = await cognee.search(
    query_text="When was Einstein born?",
    query_type=SearchType.INFORMATION
)
```

Use information search when you want to:
- Find specific facts
- Get direct answers to questions
- Retrieve precise information

### 3. RAG (Retrieval-Augmented Generation) Search

RAG search combines retrieval from your knowledge graph with generative AI to provide comprehensive answers:

```python
results = await cognee.search(
    query_text="Explain Einstein's contributions to physics",
    query_type=SearchType.RAG
)
```

Use RAG search when you want to:
- Get detailed explanations
- Combine multiple pieces of information
- Generate comprehensive answers based on your knowledge graph

### 4. Additional Search Types

Cognee offers several additional specialized search types:

- **SUMMARIES**: Get concise summaries of topics
- **CODE**: Find code-related information
- **GRAPH_COMPLETION**: Get contextually aware answers using graph traversal
- **GRAPH_SUMMARY_COMPLETION**: Combine graph traversal with summarization

For details on these and other search types, see the [Search Types Reference](../reference/search-types).

## Advanced Search Options

### Limiting Results

You can limit the number of results returned:

```python
results = await cognee.search(
    query_text="Your query",
    query_type=SearchType.INSIGHTS,
    limit=5  # Return only 5 results
)
```

### Filtering by Node Type

You can filter search results by node type:

```python
results = await cognee.search(
    query_text="Your query",
    query_type=SearchType.INSIGHTS,
    node_types=["Person", "Organization"]  # Only include these node types
)
```

### Searching with Context

You can provide additional context for your search:

```python
results = await cognee.search(
    query_text="Your query",
    query_type=SearchType.INSIGHTS,
    context="Additional context to help refine the search"
)
```

## Search Examples

### Example 1: Finding Connections Between People

```python
# Add some content
await cognee.add("Steve Jobs co-founded Apple with Steve Wozniak in 1976.")
await cognee.add("Tim Cook became CEO of Apple after Steve Jobs.")

# Process the content
await cognee.cognify()

# Search for connections
results = await cognee.search(
    query_text="What is the relationship between Steve Jobs and Tim Cook?",
    query_type=SearchType.INSIGHTS
)
```

### Example 2: Getting Specific Information

```python
# Add some content
await cognee.add("The Eiffel Tower was completed on March 31, 1889. It is 330 meters tall.")

# Process the content
await cognee.cognify()

# Search for specific information
results = await cognee.search(
    query_text="When was the Eiffel Tower completed?",
    query_type=SearchType.INFORMATION
)
```

### Example 3: Generating Comprehensive Answers

```python
# Add some content
await cognee.add("Machine learning is a subset of artificial intelligence.")
await cognee.add("Deep learning is a type of machine learning that uses neural networks.")
await cognee.add("Neural networks are computing systems inspired by biological neural networks.")

# Process the content
await cognee.cognify()

# Generate a comprehensive answer
results = await cognee.search(
    query_text="Explain the relationship between machine learning, deep learning, and neural networks",
    query_type=SearchType.RAG
)
```

## Troubleshooting Search

If you're not getting the expected search results:

1. **No results**: Make sure you've added relevant content and run `cognee.cognify()`
2. **Irrelevant results**: Try refining your query or using a different search type
3. **Too many results**: Use the `limit` parameter to reduce the number of results
4. **Missing connections**: Your knowledge graph might not have captured the relationships you're looking for; try adding more relevant content

## Next Steps

- Learn how to [visualize your knowledge graph](graph-visualization)
- Explore [Cognee Tasks](cognee-tasks) for specific use cases
- See the [Search Types Reference](../reference/search-types) for a comprehensive list of all search types
- See how to [build custom pipelines](../core-concepts/pipelines) for specialized search functionality
````

## File: content/integrations/_meta.js
````javascript
const meta = {
  cline: "Cline",
  continue: "Continue",
  "roo-code": "Roo Code",
  cursor: "Cursor",
};

export default meta;
````

## File: content/integrations/cline.mdx
````
---
title: Cline
---

export function generateMetadata() {
  return {
    title: "Cognee Integration - Cline",
    description: "Integrate cognee with Cline.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/integrations/cline",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/integrations/cline",
      type: "website",
      title: "Cognee Integration - Cline",
      description: "Integrate cognee with Cline.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Integration - Cline",
      description: "Integrate cognee with Cline.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


# Cline Integration

Cline provides a convenient interface to interact with **cognee**'s MCP server—much like [Roo](/integrations/roo-code.mdx) but with its own approach. This guide will walk you through setting up Cline in Visual Studio Code and configuring cognee's MCP server, allowing you to generate knowledge graphs from your Python projects, perform deep code searches, and more.

## Why Use Cline?

Cline is designed to make natural language interactions possible within your development environment. Instead of juggling multiple terminals or external tools, you can directly send requests to cognee through Cline to:  

- Analyze complex codebases
- Construct visual dependency maps
- Retrieve relevant code snippets for review or refactoring

By combining **Cline** and **cognee**, you get an **all-in-one** solution for deeply understanding and maintaining large repositories.

## Prerequisites

Before proceeding, ensure you have:

1. **Visual Studio Code** installed.
2. A local copy of the cognee repository.
3. An **LLM API key** (default setup requires OpenAI).

Let's get started step by step.

<details>
    <summary>1. Install Cline</summary>

1. Open **Visual Studio Code**.
2. Search for "Cline" in the Extensions panel or visit the Marketplace [here](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev).
3. Click **Install**.

> Note: After installation, you'll need to enable MCP server connections in Settings.
> 
</details>

<details>
    <summary>2. [Install](/how-to-guides/deployment/mcp) Cognee MCP Server</summary>
</details>

<details>
    <summary>3. Configure Cline to Use Cognee</summary>

Cline locates MCP servers via a configuration file, similar to how Roo does. However, you'll specify your own path for Cline's settings.

1. Open your **Cline MCP settings** file. The default location on a Mac is:
    
```
~/Library/Application\ Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json
```
You can edit the file by typing 
```
nano ~/Library/Application\ Support/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json
```

Find the current working directory where you set up the Cognee MCP server by running
```
pwd
```
    
2. Edit the file (using your preferred text editor, or simply `nano`) to add a new server entry for **Cognee**:


    
```json
{
  "mcpServers": {
    "cognee": {
      "command": "uv",
      "args": [
        "--directory",
        "/{cognee_root_path}/cognee-mcp",
        "run",
        "cognee"
      ],
      "env": {
        "ENV": "local",
        "TOKENIZERS_PARALLELISM": "false",
        "LLM_API_KEY": "sk-...}",
        "EMBEDDING_PROVIDER":"fastembed",
        "EMBEDDING_MODEL":"sentence-transformers/all-MiniLM-L6-v2",
        "EMBEDDING_DIMENSIONS":384,
        "EMBEDDING_MAX_TOKENS"256
      }
    }
  }
}
```
    
    - **`{cognee_root_path}`**: Replace with the **absolute path** to where you cloned Cognee.
    - **`LLM_API_KEY`**: Replace the placeholder with your AI provider key.

3. **Save** the file.
</details>
<details>
    <summary>4. Restart Cline</summary>

- Once the configuration is saved, **restart** Cline.
- When Cline initializes, it will detect the new Cognee server from your config file.

</details>
<details>
    <summary>4. Example - Use Cognee from Cline</summary>

1. Navigate to the **repo** you want to analyze within VS Code.
2. Make sure to enable Cline to use MCP servers by navigating to Settings and checking MCP Server Connection box
2. Open the **Cline** interface -- SHIFT+COMMAND+P <i>Cline: Open in New Tab</i>
4. Type your natural language commands one-by-one to invoke the Cognee server. 

```

    # clears the databases
    prune cognee
    # extracts structure from the repository
    run codify in this repo
    # Use the `CODE` search type to query your code graph.
    find dependencies and relationships between components with CODE search

```

Running these commands should look something like this:

<img src="/images/cline_example_1.png" alt="cline_example_1" width="600"/>

<img src="/images/cline_example_2.png" alt="cline_example_2" width="600"/>
</details>

With Cognee integrated into Cline, you can now seamlessly:

- **Generate detailed knowledge graphs** of your complex codebases.
- **Search** and manage tangled dependencies directly through natural language commands in your IDE.
- Build more advanced workflows around code analysis, refactoring, or knowledge retrieval.

### Join the Conversation!
Have questions? Join our community now to connect with professionals, share insights, and get your questions answered!
<br></br>
  <a href="https://discord.gg/m63hxKsp4p" target="_blank" rel="noopener noreferrer">
    <button className="button cta-button">
      Join the community
    </button>
  </a>
````

## File: content/integrations/continue.mdx
````
---
title: Continue
---

export function generateMetadata() {
  return {
    title: "Cognee Integration - Continue",
    description: "Integrate cognee with Continue.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/integrations/continue",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/integrations/continue",
      type: "website",
      title: "Cognee Integration - Continue",
      description: "Integrate cognee with Continue.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Integration - Continue",
      description: "Integrate cognee with Continue.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}

# Continue Integration

Continue provides a convenient interface to interact with **cognee**'s MCP server—much like [Roo](/integrations/roo-code.mdx) but with its own approach. This guide will walk you through setting up Continue in your IDE and configuring cognee's MCP server, allowing you to generate knowledge graphs from your Python projects, enhance AI code assistance, and more.

## Why Use Continue?

Continue is designed to make AI-assisted development more powerful within your IDE. Instead of working with limited context, you can leverage cognee through Continue to:  

- Get contextually aware code completions
- Enhance AI understanding of your codebase
- Improve the quality of code assistance

By combining **Continue** and **cognee**, you get an **all-in-one** solution for intelligent code understanding and AI assistance.

## Prerequisites

Before proceeding, ensure you have:

1. Your preferred **IDE** installed
2. A [Continue Hub](https://hub.continue.dev) account
3. Successfully logged into Continue in your IDE

Let's get started step by step.

<details>
    <summary>1. Install Continue</summary>

1. Open your **preferred IDE**.
2. Install Continue following the [official documentation](https://www.continue.dev).
3. Log in to your Continue Hub account.

> Note: After installation, you'll need to configure your AI providers and settings.
</details>

<details>
    <summary>2. [Install](/how-to-guides/deployment/mcp) Cognee MCP Server</summary>
</details>

<details>
    <summary>3. Configure Continue to Use Cognee</summary>

Continue offers two integration methods for working with cognee:

1. **Pre-built Assistant Option**:
   - Use the ready-made `cognee` assistant
   - Access standard knowledge graph capabilities
   - No additional configuration needed

2. **Custom Assistant Option**:
   - Build your own using the `Cognee Context Provider` block
   - Customize the integration to your specific needs
   - Requires additional configuration

Choose your preferred method and proceed with:

1. Open VSCode and use `SHIFT-COMMAND-P` (Mac)
2. Select `Continue: Open in new window`
3. In the top right corner, choose either:
   - Pre-built `cognee` assistant
   - Your custom assistant with Cognee Context Provider

</details>

<details>
    <summary>4. Restart Continue</summary>       

Restart your IDE to ensure the updated Continue configuration is applied. You should see Continue recognizing the cognee integration on startup.

     <img src="/images/continue_setup.webp" alt="continue_setup" width="600"/>

</details>

<details>
    <summary>5. Use Continue + Cognee for Enhanced Code Assistance</summary>

Once Continue is configured, you can begin leveraging cognee's capabilities:

1. Open your project and start a new Continue session to generate a knowledge graph:
    
     <img src="/images/continue_step1.webp" alt="continue_step1" width="600"/>

> Tip: For larger codebases, the initial knowledge graph generation might take some time. Subsequent uses will be faster.
>

2. Use Continue's AI assistance with enhanced context from cognee.

     <img src="/images/continue_step2.webp" alt="continue_step2" width="600"/>

3. Get more accurate and contextually aware suggestions

     <img src="/images/continue_step3.webp" alt="continue_step3" width="600"/>
</details>

### Join the Conversation!
Have questions? Join our community now to connect with professionals, share insights, and get your questions answered!
<br></br>
  <a href="https://discord.gg/m63hxKsp4p" target="_blank" rel="noopener noreferrer">
    <button className="button cta-button">
      Join the community
    </button>
  </a>
````

## File: content/integrations/cursor.mdx
````
---
title: Cursor
---

export function generateMetadata() {
  return {
    title: "Cognee Integration - Cursor",
    description: "Integrate cognee with Cursor.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/integrations/cursor",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/integrations/cursor",
      type: "website",
      title: "Cognee Integration - Cursor",
      description: "Integrate cognee with Cursor.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Integration - Cursor",
      description: "Integrate cognee with Cursor.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}

# Cursor Integration

If you’re looking to unify your code exploration in Python repositories, [**Cursor**](https://www.cursor.com/) provides an intuitive interface to interact with **cognee**’s MCP server directly. 


> If you are using Visual Studio Code, you can explore our [Roo](/integrations/roo-code.mdx) or [Cline](/integrations/cline.mdx) integration guides instead.


By integrating Cursor and cognee, you can effortlessly:

- Generate knowledge graphs from your codebase
- Access code search capabilities
- Explore advanced analysis tools without leaving your IDE

Let's quickly set up cognee’s MCP server in Cursor, ensuring you can query your codebase and retrieve insights.

## Why Use Cognee with Cursor?

**Cognee** specializes in building detailed knowledge graphs and retrieve accurate data based on user queries. Together with **Cursor**, you get:

- **Streamlined Development Experience:** Interact with cognee’s code analysis directly from Cursor’s Composer.
- **Enhanced Code Understanding:** Find out dependencies and relationships in your code base easily, and quickly search across large codebases.
- **Efficiency Gains:** No need to switch between terminals or external apps—simply invoke cognee’s powerful tools from within your IDE.


## Prerequisites

Before proceeding, ensure you have the following:

1. **Cursor** installed on your machine.
2. A local copy of the cognee repository.
3. An **LLM API key** (default setup uses OpenAI, e.g., `sk-...`).

## Integration Steps

<details>
  <summary>1. Install Cursor</summary>

1. Visit the official [Cursor website](https://www.cursor.com/) to download **Cursor**.
2. Follow the on-screen instructions to install Cursor on your operating system.
3. Once installed, open **Cursor** to verify everything is functioning properly.

</details>
<details>
  <summary>2. Clone and Navigate to Cognee</summary>

Open your terminal and run:

```bash
git clone https://www.github.com/topoteretes/cognee
cd cognee/cognee-mcp
```

</details>
<details>
  <summary>3. Install Dependencies</summary>

Cognee uses the `uv` package manager for setup and runtime:

1. If you’re on macOS, install `uv` via Homebrew:
    
    ```bash
    brew install uv
    ```
    
2. Move to the `cognee-mcp` directory and sync dependencies:
    
    ```bash
    uv sync --reinstall
    ```
    

This process ensures cognee’s environment is fully configured and ready to run.

</details>
<details>
  <summary>4. Create a Run Script for Cognee</summary>

1. Inside your preferred scripts directory (e.g., in your project directory), create a file named `run-cognee.sh`.
2. Make it executable and add the following contents:

```bash
#!/bin/bash
export ENV=local
export TOKENIZERS_PARALLELISM=false
export EMBEDDING_PROVIDER = "fastembed"
export EMBEDDING_MODEL="sentence-transformers/all-MiniLM-L6-v2"
export EMBEDDING_DIMENSIONS= 384
export EMBEDDING_MAX_TOKENS-256
export LLM_API_KEY=your-API-key
uv --directory /{cognee_root_path}/cognee-mcp run cognee
```

> Remember:
> 
> - Update `/{cognee_root_path}/cognee-mcp` to the full path of your cloned cognee repo.
> - Replace `your-API-key` with your actual API key.

</details>
<details>
  <summary>5. Add a New MCP Server in Cursor</summary>

1. Launch **Cursor**, and click the **Gear Icon** to open **Settings**.
2. Navigate to **Features > MCP**.
3. Click on **+ Add New MCP Server**.

In the **Add MCP Server** modal, set the following:

- **Type:** `Stdio`
- **Name:** `Cognee` (or any nickname you prefer)
- **Command:** Point this to your script:
    
    ```bash
    sh /{script_root_path}/run-cognee.sh
    ```
    <br></br>
    <img src="/images/cursor_servers.webp" alt="cursor_servers" width="800"/>

**Save** this configuration. You should see your new entry in the MCP settings list.

</details>
<details>
  <summary>6. Refresh and Verify Cognee in Cursor</summary>

1. In the MCP settings, locate your newly added **cognee** server.
2. Click the **Refresh** button (often in the top-right corner of the server’s card) to have Cursor attempt to connect.

If all goes well, you should see a list of **available tools** from cognee (e.g., codify). This indicates cognee’s MCP server is running correctly, and Cursor has successfully loaded the server’s capabilities.

</details>
<details>
  <summary>7. Use Cognee in Cursor’s Composer</summary>

1. Open the **Composer** in Cursor.
2. Make sure **Agent** and not **Ask** is selected.
3. Issue a prompt referencing cognee tools. Cursor will pass your request to the cognee MCP server, and results will be displayed directly in the Composer. For instance:
    
         <img src="/images/cursor_step1.webp" alt="cursor_step1" width="600"/>
         <img src="/images/cursor_step2.webp" alt="cursor_step2" width="600"/>
         <img src="/images/cursor_step3.webp" alt="cursor_step3" width="600"/>


> Remember: Use the `CODE` search type to query your code graph.
> Tip: For larger codebases, consider incremental indexing or caching to speed up analysis.
> 

</details>

You’ve now set up cognee’s MCP server with Cursor! Enjoy a richer, more powerful code exploration experience right inside your IDE.

---

### Join the Conversation!

Have questions or feedback? Join our community to connect with professionals, share insights, and get answers to your questions!

<br></br>
<a href="https://discord.gg/m63hxKsp4p" target="_blank" rel="noopener noreferrer">
<button className="button cta-button">
Join the community
</button>
</a>
````

## File: content/integrations/roo-code.mdx
````
---
title: Roo Code
---

export function generateMetadata() {
  return {
    title: "Cognee Integration - Roo Code",
    description: "Integrate cognee with Roo Code.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/integrations/roo-code",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/integrations/roo-code",
      type: "website",
      title: "Cognee Integration - Roo Code",
      description: "Integrate cognee with Roo Code.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Integration - Roo Code",
      description: "Integrate cognee with Roo Code.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


# Roo Code Integration

Roo provides a convenient interface to interact with **cognee**'s MCP server—much like [Cline](/integrations/cline.mdx) but with its own approach. This guide will walk you through setting up Roo in Visual Studio Code and configuring cognee’s MCP server, allowing you to generate knowledge graphs from your Python projects, perform deep code searches, and more.

## Why Use Roo?

Roo is designed to make natural language interactions possible within your development environment. Instead of juggling multiple terminals or external tools, you can directly send requests to cognee through Roo to:  

- Analyze complex codebases
- Construct visual dependency maps
- Retrieve relevant code snippets for review or refactoring

By combining **Roo** and **cognee**, you get an **all-in-one** solution for deeply understanding and maintaining large repositories.

## Prerequisites

Before proceeding, ensure you have:

1. **Visual Studio Code** installed.
2. A local copy of the cognee repository.
3. An **LLM API key** (default setup requires OpenAI).

Let's get started step by step.

<details>
    <summary>1. Install Roo</summary>

1. Open **Visual Studio Code**.
2. Search for “Roo” in the Extensions panel or visit the Marketplace [here](https://marketplace.visualstudio.com/items?itemName=RooVeterinaryInc.roo-cline).
3. Click **Install**.

> Note: After installation, you’ll see a Roo icon that you can use to interact with the extension.
> 
</details>
<details>
    <summary>2. [Install](/how-to-guides/deployment/mcp) Cognee MCP Server</summary>
</details>

<details>
    <summary>3. Configure Roo to Use Cognee</summary>

Roo locates MCP servers via a configuration file, similar to how Cline does. However, you’ll specify your own path for Roo’s settings.

1. Open the **Roo MCP settings** file in your home or user directory. (The exact path may vary depending on your OS or custom setup.)
2. Insert a new entry for the **cognee** server. It should look something like this:

```json
{
  "mcpServers": {
    "cognee": {
      "command": "uv",
      "args": [
        "--directory",
        "/{absolute_path_to}/cognee/cognee-mcp",
        "run",
        "cognee"
      ],
      "env": {
        "ENV": "local",
        "TOKENIZERS_PARALLELISM": "false",
        "LLM_API_KEY": "sk-",
        "EMBEDDING_PROVIDER":"fastembed",
        "EMBEDDING_MODEL":"sentence-transformers/all-MiniLM-L6-v2",
        "EMBEDDING_DIMENSIONS":384,
        "EMBEDDING_MAX_TOKENS"256
      }
    }
  }
}

```

- Replace `/{absolute_path_to}/cognee/cognee-mcp` with the full path to your cloned cognee repo.
- Enter your **LLM API key** in place of `sk-...`.
3. **Save** your settings file and exit.

</details>
<details>
    <summary>4. Restart Roo</summary>       

Click restart button in MCP servers window to ensure the updated Roo configuration is applied. You should see Roo recognizing the cognee server on startup.

     <img src="/images/roo_servers.webp" alt="roo_servers" width="600"/>

</details>

<details>
    <summary>5. Use Roo + Cognee for Code Analysis</summary>

Once Roo is configured, you can begin interacting with cognee right from your IDE:

1. Open your project in VS Code to locate the **Roo** interface and codify your codebase to generate a knowledge graph. For example:
    
     <img src="/images/roo_step1.webp" alt="roo_step1" width="600"/>

    
> Tip: For larger codebases with deep dependencies, consider setting up incremental indexing or caching to speed up repeated analyses.
>
2. Use the CODE search type to query your freshly generated knowledge graph.

     <img src="/images/roo_step2.webp" alt="roo_step2" width="600"/>

3. Get your results promptly

     <img src="/images/roo_step3.webp" alt="roo_step3" width="600"/>
</details>

### Join the Conversation!
Have questions? Join our community now to connect with professionals, share insights, and get your questions answered!
<br></br>
  <a href="https://discord.gg/m63hxKsp4p" target="_blank" rel="noopener noreferrer">
    <button className="button cta-button">
      Join the community
    </button>
  </a>
````

## File: content/reference/_meta.js
````javascript
const meta = {
  infrastructure: "Infrastructure",
  modules: "Modules",
  tasks: "Tasks",
  sdk: "SDK",
  "api-reference": "API",
  "search-types": "Search Types",
  "descriptive-metrics": "Descriptive Metrics",
  "retriever-evaluation": "Retriever Evaluation",
  "colab-notebooks": "Colab Notebooks",
  "ontology-reference": "Ontologies",
};

export default meta;
````

## File: content/reference/api-reference.mdx
````
---
title: API
---

export function generateMetadata() {
  return {
    title: "Cognee Reference - API",
    description: "Cognee api reference.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/reference/api-reference",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/reference/api-reference",
      type: "website",
      title: "Cognee Reference - API",
      description: "Cognee api reference.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Reference - API",
      description: "Cognee api reference.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


# Cognee API Reference

## Overview

The Cognee API provides a comprehensive set of functions and endpoints for building, managing, and querying knowledge graphs. This reference outlines both the Python API functions and the HTTP REST API endpoints.

## Core Python API Functions

### Data Management

```python
# Add content to Cognee
await cognee.add(content)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `content` | `str` | Text content, file path (using `file://` prefix), or URL to add to the knowledge graph |

```python
# Process content and build the knowledge graph
await cognee.cognify()
```

```python
# Reset data and system state
await cognee.prune.prune_data()  # Reset just the data
await cognee.prune.prune_system(metadata=True)  # Reset system state
await cognee.prune.prune_all()  # Reset everything
```

### Search and Query

```python
# Search the knowledge graph
from cognee.modules.search.types import SearchType

results = await cognee.search(
    query_text="Your search query",
    query_type=SearchType.INSIGHTS,  # or INFORMATION, RAG, etc.
    limit=10
)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `query_text` | `str` | The search query text |
| `query_type` | `SearchType` | Type of search to perform (see [Search Types Reference](search-types) for all options) |
| `limit` | `int` | Maximum number of results to return |

> **Note:** For a comprehensive reference of all available search types, see the [Search Types Reference](search-types).

### Graph Visualization

```python
import cognee.api.v1 as api

# Generate an HTML visualization of your graph
visualization_path = await api.render_graph()
```

The visualization is saved as an HTML file in the `.cognee_system` folder.

### Configuration

```python
# Configure Cognee
import cognee

# LLM configuration
cognee.config.llm_api_key = "YOUR_API_KEY"
cognee.config.llm_model = "gpt-4"  # Default model

# Database configuration
cognee.config.db_provider = "sqlite"  # or "postgres"
cognee.config.db_connection_string = "postgresql://user:password@localhost:5432/cognee"
```

## HTTP REST API

The Cognee HTTP API provides RESTful endpoints for interacting with your knowledge graph from any application.

### Interactive API Documentation

Below is the interactive API documentation generated from our OpenAPI specification:

import { ApiDocumentation } from "../../components/ApiDocumentation";

<ApiDocumentation />

### Key Endpoints

- **POST /api/v1/add**: Add content to the knowledge graph
- **POST /api/v1/cognify**: Process content and build the knowledge graph
- **POST /api/v1/search**: Search the knowledge graph
- **GET /api/v1/render_graph**: Generate a visualization of the knowledge graph
- **POST /api/v1/prune**: Reset data and system state

## Using the API in Your Applications

### Python Example

```python
import cognee
import asyncio

async def main():
    # Configure
    cognee.config.llm_api_key = "YOUR_API_KEY"
    
    # Add content
    await cognee.add("Your content here")
    
    # Process
    await cognee.cognify()
    
    # Search
    from cognee.modules.search.types import SearchType
    results = await cognee.search("Your query", query_type=SearchType.INSIGHTS)
    
    # Visualize
    import cognee.api.v1 as api
    visualization_path = await api.render_graph()
    
if __name__ == "__main__":
    asyncio.run(main())
```

### HTTP API Example

```python
import requests

# Add content
requests.post(
    "http://localhost:8000/api/v1/add",
    json={"content": "Your content here"}
)

# Process
requests.post("http://localhost:8000/api/v1/cognify")

# Search
response = requests.post(
    "http://localhost:8000/api/v1/search",
    json={
        "query_text": "Your query",
        "query_type": "INSIGHTS",
        "limit": 10
    }
)
results = response.json()
```

## Understanding Graph Visualization

The graph visualization shows:

- **Nodes**: Entities extracted from your content (people, places, concepts, etc.)
- **Edges**: Relationships between entities
- **Categories**: Nodes are colored by category (e.g., person, location, organization)

The visualization helps you understand how different pieces of information are connected in your knowledge graph.

## Next Steps

- Check out the [SDK Reference](sdk_reference) for more detailed information
- Explore the [Search Types Reference](search-types) for all available search options
- Learn about [Pipelines](../core-concepts/pipelines) for advanced usage
- Explore [Cognee Tasks](../how-to-guides/cognee-tasks) for specific use cases
````

## File: content/reference/colab-notebooks.mdx
````
---
title: Colab Notebooks
---

export function generateMetadata() {
  return {
    title: "Cognee Reference - Colab Notebooks",
    description: "Cognee colab notebooks reference.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/reference/colab-notebooks",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/reference/colab-notebooks",
      type: "website",
      title: "Cognee Reference - Colab Notebooks",
      description: "Cognee colab notebooks reference.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Reference - Colab Notebooks",
      description: "Cognee colab notebooks reference.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


This is a centralized hub for collaborative and example notebooks designed to showcase cognee's features and integration workflows. These notebooks provide hands-on examples through cognee's tasks.
Each notebook includes a real-world use case example and expected outputs to help you integrate cognee seamlessly into your projects.


### Available Notebooks
1. [**cognee Demo**](https://github.com/topoteretes/cognee/blob/291f1c5a55abacdef3356fabd37ee0a677db34e1/notebooks/cognee_demo.ipynb): A demo showcasing cognee’s capabilities, including data ingestion, knowledge graph creation, and queries.
2. [**cognee Code Graph Demo**](https://github.com/topoteretes/cognee/blob/291f1c5a55abacdef3356fabd37ee0a677db34e1/notebooks/cognee_code_graph_demo.ipynb): This notebook demonstrates how to create a code-centric knowledge graph using cognee, showcasing connections between programming concepts and their relationships.
3. [**cognee Hotpot Evaluation**](https://github.com/topoteretes/cognee/blob/291f1c5a55abacdef3356fabd37ee0a677db34e1/notebooks/cognee_hotpot_eval.ipynb): Explore how cognee integrates with datasets and performs HotpotQA-style question-answering evaluations using structured data.
4. [**cognee Llama Index**](https://github.com/topoteretes/cognee/blob/291f1c5a55abacdef3356fabd37ee0a677db34e1/notebooks/cognee_llama_index.ipynb): Learn how to use the Llama Index with cognee to enhance graph-based search and retrieval tasks, enabling more efficient information discovery.
5. [**cognee Multimedia Demo**](https://github.com/topoteretes/cognee/blob/291f1c5a55abacdef3356fabd37ee0a677db34e1/notebooks/cognee_multimedia_demo.ipynb): This notebook demonstrates how to integrate and process multimedia data (e.g., images, audio) within cognee’s pipelines to generate insights and graphs.
6. [**cognee HR Demo**](https://github.com/topoteretes/cognee/blob/291f1c5a55abacdef3356fabd37ee0a677db34e1/notebooks/hr_demo.ipynb): Focused on human resources use cases, this notebook illustrates how cognee helps in analyzing resumes, job descriptions, and matching candidates to roles.

### How to Use These Notebooks
- **Select a Notebook:** Choose a notebook based on your use case or learning goals.
- **Set Up the Environment:** Follow the prerequisites in each notebook to configure dependencies.
- **Run and Explore:** Open the notebook, run the cells, and observe how cognee processes data to generate insights.
- **Customize and Extend:** Modify the examples to fit your specific project needs.

#### How to Contribute
If you have a notebook showcasing an innovative way to use cognee, we’d love to include it! Submit a pull request to our [GitHub repository](https://github.com/topoteretes/cognee) or reach out to us directly.
<br></br>
  <a href="https://discord.gg/m63hxKsp4p" target="_blank" rel="noopener noreferrer">
    <button className="button cta-button">
      Join the community
    </button>
  </a>
````

## File: content/reference/descriptive-metrics.mdx
````
---
title: Descriptive Metrics
---

export function generateMetadata() {
  return {
    title: "Cognee Reference - Descriptive Metrics",
    description: "Cognee descriptive metrics reference.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/reference/descriptive-metrics",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/reference/descriptive-metrics",
      type: "website",
      title: "Cognee Reference - Descriptive Metrics",
      description: "Cognee descriptive metrics reference.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Reference - Descriptive Metrics",
      description: "Cognee descriptive metrics reference.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


## Metrics
Below is a list of descriptive metrics calculated for graph correctness and quality assessment. 
All calculations convert the graph into an undirected graph, meaning edge direction is not considered in path-related metrics.

### **1. Token & Graph Size Metrics**
- **`num_tokens`**: Total number of tokens in the input text.
- **`num_nodes`**: Total number of nodes (entities) in the knowledge graph.
- **`num_edges`**: Total number of edges (relationships) connecting nodes.

### **2. Connectivity & Density Metrics**
- **`mean_degree`**: Average number of edges per node.
- **`edge_density`**: Ratio of existing edges to the maximum possible edges, measuring graph sparsity.
- **`num_connected_components`**: Number of connected components; higher values may indicate fragmentation.
- **`sizes_of_connected_components`**: Number of nodes in each connected component.

### **3. Structural Integrity Metrics**
- **`num_selfloops`**: Number of self-loops (nodes connected to themselves); may indicate errors.
- **`diameter`**: The longest shortest path between any two nodes in the graph.
- **`avg_shortest_path_length`**: The average shortest path between all node pairs, indicating graph efficiency.
- **`avg_clustering`**: Average clustering coefficient, measuring the likelihood of nodes forming tightly connected groups.

## Interpreting the Metrics

When analyzing these metrics, certain extreme values may indicate potential issues, e.g.:

- **Number of input tokens in relation to graph size** : Large input documents with only a few generated nodes indicates discrepancy.
- **Mean Degree** : A value of 1 suggests an extremely sparse graph, while a value too close to num_nodes suggests excessive connectivity. Since multiple edges can exist between two nodes, it is possible for the mean degree to be higher than num_nodes, but an unusually high value should be investigated.
- **Diameter**: Extreme values such as 1 (a fully connected graph) or num_nodes-1 (a path) clearly indicate issues.

The following table presents examples of graphs with 50 nodes that exhibit extreme values for diameter and mean degree. 
These cases illustrate how structural properties can vary widely, from highly connected graphs with small diameters to sparse graphs with minimal connectivity — configurations that are unlikely to correspond to real-world knowledge graphs, which typically balance connectivity and semantic structure to preserve meaningful relationships.

|  | Too dense | Correct | Too sparse |
|----------|----------|----------|----------|
|Mean degree| 49  | 3.52  | 1.96 |
|Diameter| 1 | 9  | 49  |
|   | <img src="/images/fully_connected_graph.png" alt="Fully connected graph" width="200"></img>  |<img src="/images/normal_graph.png" alt="Correct graph" width="200"></img> | <img src="/images/path_graph.png" alt="Path" width="200"></img>  |


#### Tracking Changes Over Time:

Beyond analyzing static graphs, monitoring how these metrics evolve over time can reveal important insights about structural shifts. 
Unexpected deviations may indicate potential issues. 

- Adding new data should increase the number of nodes.
- Adding information about existing entities should increase the number of edges and edge density.
- If new data is loosely related to existing data, the diameter may increase.
- If new data strengthens existing entity relationships, the diameter may decrease.

For a quick visual explanation of these graph metrics and their implications, [**click here**](https://www.youtube.com/shorts/4cN1jOEnpcc)

For generating graph metrics, see our [Descriptive Metrics](/core-concepts/graph-generation/descriptive-metrics) documentation.
````

## File: content/reference/infrastructure.mdx
````
---
title: Infrastructure
---

export function generateMetadata() {
  return {
    title: "Cognee Reference - Infrastructure",
    description: "Cognee infrastructure reference.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/reference/infrastructure",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/reference/infrastructure",
      type: "website",
      title: "Cognee Reference - Infrastructure",
      description: "Cognee infrastructure reference.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Reference - Infrastructure",
      description: "Cognee infrastructure reference.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


# Infrastructure

## System Requirements

- **Python Environment:** Cognee supports Python 3.9+
- **Node.js & npm:** Required if you intend to run the frontend UI locally

## Core Infrastructure Components

Configure these in environment variables or `.env` files.

### Vector Stores

Cognee supports multiple vector store backends, which handle vector embeddings for semantic search and context retrieval:

- **LanceDB** (default local vector database)
- **PGVector** (PostgreSQL extension)
- **Qdrant**
- **Weaviate**
- **Milvus**

### Graph Databases

Cognee builds a knowledge graph from extracted entities and relationships:

- **NetworkX** (default in-memory graph database)
- **Kuzu** (performant in-memory graph database)
- **Neo4j**

### Relational Databases

Cognee supports:

- **SQLite** (default local relational database)
- **PostgreSQL**

### LLM Providers and Cognitive Services

Cognee leverages LLMs to process, classify, and summarize text. By default, it expects an OpenAI-compatible API key but can also integrate with other providers.

**Remote Providers:**
- OpenAI
- Anthropic
- Gemini
- Anyscale
- Openrouter

**Local Providers:**
- Ollama (recommended: phi4, llama3.3 70b-instruct-q3_K_M, deepseek-r1:32b)

### Visualization

We provide you with default visualization but you can also use:
- **Graphistry** for advanced graph visualization with **NetworkX**
- **Neo4j** browser interface
- **Kuzu** native interface

## Telemetry

Cognee includes robust telemetry support to help you monitor, analyze, and improve your workflows. Telemetry tools provide detailed insights into system performance, user interactions, and data flows, enabling continuous optimization.

### Current Support

**Langfuse:** Integration with Langfuse enables real-time monitoring and logging for AI-powered workflows, helping you trace and debug pipeline performance effectively.

### Upcoming Support

**Langraph:** Planned integration with Langraph will add advanced graph-based telemetry capabilities, allowing for more detailed visualization and analysis of system behaviors and relationships.

> Stay tuned for updates as we expand telemetry support to provide even greater observability and insights into your cognee-powered applications.
````

## File: content/reference/modules.mdx
````
---
title: Modules
---

export function generateMetadata() {
  return {
    title: "Cognee Reference - Modules",
    description: "Cognee modules reference.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/reference/modules",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/reference/modules",
      type: "website",
      title: "Cognee Reference - Modules",
      description: "Cognee modules reference.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Reference - Modules",
      description: "Cognee modules reference.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


# Project Modules Documentation

This document provides an overview of the modules in the project, their purposes, and the key functionalities they handle.

---

## **1. Settings Module**
Handles configuration and settings management for the system.

- `save_llm_config.py`: Saves configuration for language model settings.
- `save_vector_db_config.py`: Saves settings for vector database configurations.
- `get_settings.py`: Retrieves general settings.
- `get_current_settings.py`: Retrieves the currently active settings.

---

## **2. Ingestion Module**
Manages data ingestion, classification, and identification processes.

- `save_data_to_file.py`: Saves ingested data to files.
- `classify.py`: Classifies datasets during ingestion.
- `discover_directory_datasets.py`: Discovers datasets in specified directories.
- `get_matched_datasets.py`: Retrieves datasets matching specific criteria.
- `identify.py`: Identifies data characteristics.
- **Submodule: `data_types`**:
  - `TextData.py`: Handles text data ingestion.
  - `BinaryData.py`: Manages binary data ingestion.
  - `IngestionData.py`: Defines generic ingestion data structures.
- **Submodule: `exceptions`**:
  - `exceptions.py`: Defines custom exceptions for ingestion-related issues.

---

## **3. Graph Module**
Focuses on graph-related operations, including graph creation, manipulation, and utility functions.

- **Submodule: `utils`**:
  - Utility scripts for node and edge handling, such as:
    - `convert_node_to_data_point.py`
    - `deduplicate_nodes_and_edges.py`
- **Submodule: `cognee_graph`**:
  - Core graph handling, including:
    - `CogneeGraph.py`: Main graph class.
    - `CogneeAbstractGraph.py`: Abstract base for graph implementations.
- **Submodule: `models`**:
  - `EdgeType.py`: Defines edge types within the graph.
- **Submodule: `exceptions`**:
  - `exceptions.py`: Custom exceptions for graph operations.

---

## **4. Pipelines Module**
The **pipelines** module is designed to facilitate the execution and management of workflows, consisting of interconnected tasks. It provides tools for defining tasks, organizing them into pipelines, executing them sequentially or in parallel, and monitoring their execution status.

- `models/`: Defines pipeline and task models.
- `operations/`: Contains operations for running tasks, parallelization, logging pipeline statuses, and retrieving pipeline states.

---

## **5. Chunking Module**
Handles text chunking for processing and storage.

- `TextChunker.py`: Main chunking logic.
- `models/DocumentChunk.py`: Defines the structure of document chunks.

---

## **6. Cognify Module**
Handles configuration and initialization of the system.

- `config.py`: System configuration settings.

---

## **7. Search Module**
Manages search functionality, including query and result logging.

- `models/`: Defines search-related models like `Query` and `Result`.
- `operations/`: Includes scripts for handling queries and results.

---

## **8. Retrieval Module**
Handles retrieval operations.

- `description_to_codepart_search.py`: Maps descriptions to code parts.
- `brute_force_triplet_search.py`: Implements a brute-force approach to triplet searches.

---

## **9. Users Module**
Manages user-related functionality, including authentication, permissions, and user data.

- **Submodule: `methods`**:
  - Handles user-related operations such as creation, deletion, and authentication.
- **Submodule: `models`**:
  - Defines user-related models, including `User`, `Group`, and `Permission`.
- **Submodule: `permissions`**:
  - Manages permissions on documents and resources.
- **Submodule: `exceptions`**:
  - Custom exceptions for user-related operations.
- **Submodule: `authentication`**:
  - Handles user authentication mechanisms.

---

## **10. Data Module**
Handles data operations, processing, and management.

- **Submodule: `methods`**:
  - Includes dataset and data management scripts.
- **Submodule: `processing`**:
  - Processes document types like `ImageDocument`, `AudioDocument`, and `TextDocument`.
- **Submodule: `operations`**:
  - Operations like translation, language detection, and metadata handling.
- **Submodule: `extraction`**:
  - Extracts topics, summaries, and categories.
  - Includes knowledge graph extraction utilities.

---

## **11. Engine Module**
Provides utilities and models for system operations.

- **Submodule: `utils`**:
  - Node and edge generation utilities.
- **Submodule: `models`**:
  - Defines entities and their types.

---

For further details on each module, refer to the inline documentation and comments within the respective files.
````

## File: content/reference/ontology-reference.mdx
````
---
title: Ontologies
---

export function generateMetadata() {
  return {
    title: "Cognee Reference - Ontologies",
    description: "Cognee ontologies reference.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/reference/ontology-reference",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/reference/ontology-reference",
      type: "website",
      title: "Cognee Reference - Ontologies",
      description: "Cognee ontologies reference.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Reference - Ontologies",
      description: "Cognee ontologies reference.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


This document provides an overview of the ontology related modules, their purposes and the key functionalities they handle.
### OntologyResolver
1. [**OntologyResolver class**](https://github.com/topoteretes/cognee/blob/dev/cognee/modules/ontology/rdf_xml/OntologyResolver.py): Implements the rdf_xml connection logic and contains the following steps
  - Utility functions to handle the lookup table, such as:
    - `build_lookup`: Creates a lookup from the ontology
    - `refresh_lookup`: Updates lookup with the latest ontology changes
  - Node - Ontology matching logic:
    - `find_closest_match`: Finds the closest ontology node to the parameter (entity -- individual, entity_type -- class)
  - Ontology subgraph collection logic:
    - `get_subgraph`: Collects the subgraph starting from the closest ontology node match

2. [**expand_with_nodes_and_edges**](https://github.com/topoteretes/cognee/blob/dev/cognee/modules/graph/utils/expand_with_nodes_and_edges.py): Implements the main graph matching logic
  - The task creates the entities and entity types from the documentchunks, looks for matching ontology nodes using the `OntologyResolver` class, and merges the structure of the matching ontology subgraphs with the LLM generated structures.


#### How to Contribute
If you have additional examples or innovative approaches to ontology integration using owl2ready, we’d love to include them! Submit a pull request to our [GitHub repository](https://github.com/topoteretes/cognee) or reach out to us directly.
<br></br>
  <a href="https://discord.gg/m63hxKsp4p" target="_blank" rel="noopener noreferrer">
    <button className="button cta-button">
      Join the community
    </button>
  </a>
````

## File: content/reference/retriever-evaluation.mdx
````
---
title: Retriever Evaluation
---

export function generateMetadata() {
  return {
    title: "Cognee Reference - Retriever Evaluation",
    description: "Cognee retriever evaluation reference.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/reference/retriever-evaluation",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/reference/retriever-evaluation",
      type: "website",
      title: "Cognee Reference - Retriever Evaluation",
      description: "Cognee retriever evaluation reference.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Reference - Retriever Evaluation",
      description: "Cognee retriever evaluation reference.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


## Evaluating the Retriever
In order to ensure optimal performance, we continuously refine all parts of the Cognee pipeline.
To assess the quality of the retrieval step, we are evaluating it using two key metrics:

### **1. Context Coverage Score**

Parameters: 
- **`golden_context`**
- **`retrieval_context`**

Coverage score takes a retrieved context and compares it to the golden context (e.g., from datasets like HotPotQA). 
This is done using a Question-Answer Generation (QAG) framework, where an LLM generates a set of close-ended (yes/no) questions from the golden context. 
The system then checks whether the retrieved context can answer these questions correctly.

The coverage score is calculated as the percentage of assessment questions where both the golden context and the retrieved context provide the same answer. 
A higher score indicates that the retrieved context contains sufficient detail to match the key information from the golden context. 

Our approach to measuring Coverage is inspired by Deepeval's [Summarization Score](https://docs.confident-ai.com/docs/metrics-summarization), where Coverage is one of the key components. 
Please refer to their [blog post](https://www.confident-ai.com/blog/a-step-by-step-guide-to-evaluating-an-llm-text-summarization-task) for a step-by-step explanation.

### **2. DeepEval's [Contextual Relevancy Metric](https://docs.confident-ai.com/docs/metrics-contextual-relevancy)**

Parameters: 
- **`input`**
- **`retrieval_context`**

Contextual relevancy measures how well the retrieved documents align with the given input (query). 
DeepEval uses an LLM-as-a-judge approach, where an LLM extracts all statements from the retrieved content and classifies each one as relevant or not. 
The Contextual Relevancy score is then calculated as the ratio of relevant statements to the total number of statements.

#### Join the Conversation!
Join our community now to connect with professionals, share insights, and get your questions answered!
<br></br>
  <a href="https://discord.gg/m63hxKsp4p" target="_blank" rel="noopener noreferrer">
    <button className="button cta-button">
      Join the community
    </button>
  </a>
````

## File: content/reference/sdk.mdx
````
---
title: SDK
---

export function generateMetadata() {
  return {
    title: "Cognee Reference - SDK",
    description: "Cognee sdk reference.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/reference/sdk",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/reference/sdk",
      type: "website",
      title: "Cognee Reference - SDK",
      description: "Cognee sdk reference.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Reference - SDK",
      description: "Cognee sdk reference.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


# Cognee SDK Reference

---
description: Overview of the Cognee core classes, functions, and modules included in the Cognee SDK.
---

This reference provides an overview of the core classes, functions, and modules included in the Cognee SDK. It serves as a starting point for developers to understand the building blocks of Cognee, how to integrate with its pipelines and tasks, and how to manage data flow using Datapoints.

> **Note:** This is a conceptual reference. For the most accurate and up-to-date details, refer to the official Cognee documentation and source code repository.

## Table of Contents

- [Core Concepts](#core-concepts)
  - [Tasks](#tasks)
  - [Pipelines](#pipelines)
  - [Datapoints](#datapoints)
- [Modules](#modules)
  - [cognee](#cognee)
  - [cognee.api.v1](#cogneeapiv1)
  - [cognee.prune](#cogneeprune)
  - [cognee.add](#cogneeadd)
- [Classes & Functions](#classes--functions)
  - [Task](#task)
  - [Pipeline](#pipeline)
  - [Datapoint Models](#datapoint-models)
  - [High-Level Methods](#high-level-methods)

---

## Core Concepts

### Tasks
**Tasks** are atomic units of work. A task:
- Accepts input data (as typed `pydantic` models).
- Transforms the data.
- Returns output data (as typed `pydantic` models).

Tasks can perform operations such as:
- Chunking text
- Generating embeddings
- Classifying entities
- Inferring relationships between nodes

### Pipelines
**Pipelines** are sequences of tasks orchestrated to perform a complex workflow. By connecting multiple tasks, you form a pipeline that ingests raw data, processes it, and outputs structured, meaningful artifacts (e.g., a knowledge graph).

Key points:
- Pipelines ensure that the output of one task is the valid input of the next.
- Pipelines allow you to version, maintain, and scale complex data flows.

### Datapoints
**Datapoints** are `pydantic` models used as standardized input/output schemas for tasks. They:
- Define the shape of data passing between tasks.
- Provide validation and consistent typing.
- Make pipelines more robust and maintainable by catching schema errors early.

---

## Modules

### `cognee`

The core module that provides high-level entry points to Cognee functionalities:
- `cognee.add(text: str)`: Add text documents to the metastore.
- `cognee.cognify()`: Run the default pipeline to generate a knowledge graph from ingested data.
- `cognee.search(...)`: Query the knowledge graph or embeddings.
- `cognee.prune`: Utilities to reset or prune data and system states.

### `cognee.api.v1`

Contains HTTP API endpoints and related logic for:
- Searching and retrieving insights.
- Managing knowledge graphs, embeddings, and document states through REST APIs.
- Integrating Cognee into your applications with a web-based interface.

Key submodules and functions:
- `cognee.api.v1.search.SearchType`: Enums for specifying different search modes (e.g., INSIGHTS, COMPLETION).

### `cognee.prune`

Provides functions to reset or prune data:
- `cognee.prune.prune_data()`: Clears stored data (documents, embeddings, graph nodes).
- `cognee.prune.prune_system(metadata=True)`: Clears system metadata, allowing a “clean slate” before running a new pipeline.

### `cognee.add`

Functionality for adding raw data into Cognee’s metastore:
- `cognee.add(text: str)`: Ingest textual data for later processing.
- Future expansions may include adding different data types (e.g., code, HTML, or binary documents after conversion).

---

## Classes & Functions

### Task

**Definition:**
```python
from cognee import Task

class MyCustomTask(Task):
    def run(self, input_datapoint: InputModel) -> OutputModel:
        # Custom logic here
        return OutputModel(...)
````

## File: content/reference/search-types.mdx
````
---
title: Search Types
---

export function generateMetadata() {
  return {
    title: "Cognee Reference - Search Types",
    description: "Cognee search types reference.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/reference/search-types",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/reference/search-types",
      type: "website",
      title: "Cognee Reference - Search Types",
      description: "Cognee search types reference.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Reference - Search Types",
      description: "Cognee search types reference.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}

# Search Types Reference

Cognee provides a variety of search types to query your knowledge graph in different ways. This reference guide explains each search type, its purpose, and how to use it effectively.

## Available Search Types

Cognee offers the following search types through the `SearchType` enum:

```python
from cognee.modules.search.types import SearchType

# Available search types
SearchType.SUMMARIES
SearchType.INSIGHTS
SearchType.CHUNKS
SearchType.INFORMATION  # Alias for CHUNKS in some contexts
SearchType.COMPLETION
SearchType.GRAPH_COMPLETION
SearchType.GRAPH_SUMMARY_COMPLETION
SearchType.CODE
SearchType.RAG  # Alias for COMPLETION in some contexts
```

## Basic Search Syntax

All search types use the same basic function call pattern:

```python
import cognee
from cognee.modules.search.types import SearchType

results = await cognee.search(
    query_text="Your search query",
    query_type=SearchType.INSIGHTS,  # Replace with your desired search type
    limit=10  # Optional: limit the number of results
)
```

## Detailed Search Type Descriptions

### SUMMARIES

The `SUMMARIES` search type retrieves summarized information from your knowledge graph.

```python
results = await cognee.search(
    query_text="Summarize what is known about quantum computing",
    query_type=SearchType.SUMMARIES
)
```

**Best for:**
- Getting concise overviews of topics
- Summarizing large amounts of information
- Quick understanding of complex subjects

### INSIGHTS

The `INSIGHTS` search type discovers connections and relationships between entities in your knowledge graph.

```python
results = await cognee.search(
    query_text="What is the relationship between Einstein and Germany?",
    query_type=SearchType.INSIGHTS
)
```

**Best for:**
- Discovering how entities are connected
- Understanding relationships between concepts
- Exploring the structure of your knowledge graph

### CHUNKS / INFORMATION

The `CHUNKS` search type (also available as `INFORMATION` in some contexts) retrieves specific facts and information chunks from your knowledge graph.

```python
results = await cognee.search(
    query_text="When was Einstein born?",
    query_type=SearchType.CHUNKS  # or SearchType.INFORMATION
)
```

**Best for:**
- Finding specific facts
- Getting direct answers to questions
- Retrieving precise information

### COMPLETION / RAG

The `COMPLETION` search type (also available as `RAG` in some contexts) uses retrieval-augmented generation to provide comprehensive answers based on your knowledge graph.

```python
results = await cognee.search(
    query_text="Explain Einstein's contributions to physics",
    query_type=SearchType.COMPLETION  # or SearchType.RAG
)
```

**Best for:**
- Getting detailed explanations
- Combining multiple pieces of information
- Generating comprehensive answers

### GRAPH_COMPLETION

The `GRAPH_COMPLETION` search type leverages the graph structure to provide more contextually aware completions.

```python
results = await cognee.search(
    query_text="How do quantum computers differ from classical computers?",
    query_type=SearchType.GRAPH_COMPLETION
)
```

**Best for:**
- Complex queries requiring graph traversal
- Questions that benefit from understanding relationships
- Queries where context from connected entities matters

### GRAPH_SUMMARY_COMPLETION

The `GRAPH_SUMMARY_COMPLETION` search type combines graph traversal with summarization to provide concise but comprehensive answers.

```python
results = await cognee.search(
    query_text="Summarize the key developments in AI from 2010 to 2023",
    query_type=SearchType.GRAPH_SUMMARY_COMPLETION
)
```

**Best for:**
- Getting summarized information that requires understanding relationships
- Complex topics that need concise explanations
- Queries that benefit from both graph structure and summarization

### CODE

The `CODE` search type is specialized for retrieving and understanding code-related information from your knowledge graph.

```python
results = await cognee.search(
    query_text="How to implement a binary search tree in Python",
    query_type=SearchType.CODE
)
```

**Best for:**
- Code-related queries
- Programming examples and patterns
- Technical documentation searches

## Advanced Usage

### Combining Search Types

For complex queries, you might want to use multiple search types in sequence:

```python
# First get insights about relationships
insights = await cognee.search(
    query_text="Relationship between quantum computing and cryptography",
    query_type=SearchType.INSIGHTS
)

# Then get a detailed explanation
explanation = await cognee.search(
    query_text=f"Explain how quantum computing affects cryptography, considering: {insights}",
    query_type=SearchType.GRAPH_COMPLETION
)
```

### Search with Filters

You can filter search results by node type or other properties:

```python
# Search only for people and organizations
results = await cognee.search(
    query_text="Who founded Microsoft?",
    query_type=SearchType.INSIGHTS,
    node_types=["Person", "Organization"]
)
```

### Limiting Results

Control the number of results returned:

```python
# Get only the top 5 results
results = await cognee.search(
    query_text="Advances in machine learning",
    query_type=SearchType.SUMMARIES,
    limit=5
)
```

## Choosing the Right Search Type

Here's a quick guide to help you choose the most appropriate search type:

| If you want to... | Use this search type |
|-------------------|----------------------|
| Get a quick summary | `SUMMARIES` |
| Discover relationships | `INSIGHTS` |
| Find specific facts | `CHUNKS` / `INFORMATION` |
| Get detailed explanations | `COMPLETION` / `RAG` |
| Understand complex relationships | `GRAPH_COMPLETION` |
| Get concise answers about complex topics | `GRAPH_SUMMARY_COMPLETION` |
| Find code examples or technical information | `CODE` |

## Examples

### Example 1: Research Paper Analysis

```python
# Add research papers to your knowledge graph
await cognee.add("file:///path/to/research_paper1.pdf")
await cognee.add("file:///path/to/research_paper2.pdf")

# Process the content
await cognee.cognify()

# Get a summary of the key findings
summaries = await cognee.search(
    query_text="Summarize the key findings from these research papers",
    query_type=SearchType.SUMMARIES
)

# Discover relationships between concepts
insights = await cognee.search(
    query_text="What is the relationship between the methodologies used in these papers?",
    query_type=SearchType.INSIGHTS
)

# Get a comprehensive analysis
analysis = await cognee.search(
    query_text="Provide a comprehensive analysis of how these papers contribute to the field",
    query_type=SearchType.GRAPH_COMPLETION
)
```

### Example 2: Code Documentation

```python
# Add code documentation to your knowledge graph
await cognee.add("file:///path/to/codebase")

# Process the content
await cognee.cognify()

# Find specific code examples
code_examples = await cognee.search(
    query_text="How to implement authentication in this codebase",
    query_type=SearchType.CODE
)

# Understand the architecture
architecture = await cognee.search(
    query_text="Explain the overall architecture of this codebase",
    query_type=SearchType.GRAPH_SUMMARY_COMPLETION
)
```

## Troubleshooting

If you're not getting the expected search results:

1. **No results**: Make sure you've added relevant content and run `cognee.cognify()`
2. **Irrelevant results**: Try refining your query or using a different search type
3. **Too many results**: Use the `limit` parameter to reduce the number of results
4. **Missing connections**: Your knowledge graph might not have captured the relationships you're looking for; try adding more relevant content

## Next Steps

- Learn how to [visualize your knowledge graph](../how-to-guides/graph-visualization)
- Explore [Cognee Tasks](../how-to-guides/cognee-tasks) for specific use cases
- See how to [build custom pipelines](../core-concepts/pipelines) for specialized search functionality
````

## File: content/reference/tasks.mdx
````
---
title: Tasks
---

export function generateMetadata() {
  return {
    title: "Cognee Reference - Tasks",
    description: "Cognee tasks reference.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/reference/tasks",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/reference/tasks",
      type: "website",
      title: "Cognee Reference - Tasks",
      description: "Cognee tasks reference.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Reference - Tasks",
      description: "Cognee tasks reference.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


Cognee organizes tasks into pipelines that populate graph and vector stores. These tasks analyze and enrich data, enhancing the quality of answers produced by Large Language Models (LLMs).

This section provides a template to help you structure your data and build pipelines. \
These tasks serve as a starting point for using Cognee to create reliable LLM pipelines.

## **1. Ingestion Tasks**
Handles the ingestion of data, including metadata, transformation, and storage.

- **`save_data_item_to_storage.py`**: Saves individual data items to the storage system.
- **`ingest_data_with_metadata.py`**: Ingests data along with its associated metadata.
- **`save_data_to_storage.py`**: Saves bulk data to the storage system.
- **`get_dlt_destination.py`**: Resolves the destination for data load transformations.
- **`resolve_data_directories.py`**: Resolves directories for data ingestion.
- **`ingest_data.py`**: Main task for ingesting data into the system.
- **`transform_data.py`**: Transforms ingested data for further processing.
- **`save_data_item_with_metadata_to_storage.py`**: Saves individual data items along with metadata to storage.

---

## **2. Temporal Awareness Tasks**
Adds temporal context to graphs and searches.

- **`build_graph_with_temporal_awareness.py`**: Constructs graphs with temporal context for nodes and edges.
- **`search_graph_with_temporal_awareness.py`**: Searches graphs considering temporal aspects.

---

## **3. Summarization Tasks**
Handles summarization of text and code.

- **`summarize_code.py`**: Generates summaries for code files.
- **`query_summaries.py`**: Queries existing summaries for specific contexts.
- **`summarize_text.py`**: Summarizes text documents.

---

## **4. Dataset Generation Tasks**
Generates golden datasets for training and evaluation.

- **`generate_golden_set.py`**: Creates a "golden set" of data for benchmarking or testing.

---

## **5. Graph Tasks**
Manages graph extraction, querying, and ontology inference.

- **`extract_graph_from_code.py`**: Extracts graph representations from codebases.
- **`infer_data_ontology.py`**: Infers ontologies and relationships from graph data.
- **`query_graph_connections.py`**: Queries connections and relationships within graphs.
- **`extract_graph_from_data.py`**: Extracts graphs from structured and unstructured data.

---

## **6. Code Dependency Tasks**
Analyzes and enriches dependency graphs for code repositories.

- **`expand_dependency_graph_checker.py`**: Expands existing dependency graphs.
- **`get_repo_dependency_graph_checker.py`**: Retrieves dependency graphs for repositories.
- **`enrich_dependency_graph_checker.py`**: Enriches dependency graphs with additional context.
- **`get_local_dependencies_checker.py`**: Identifies local dependencies within code repositories.

---

## **7. Completion Tasks**
Handles completion queries and exceptions.

- **`query_completion.py`**: Processes and handles completion requests.
- **`exceptions.py`**: Defines exceptions related to completion tasks.

---

## **8. Chunking Tasks**
Manages chunking of text into smaller, processable units.

- **`chunk_naive_llm_classifier.py`**: Classifies text chunks using a naive LLM-based approach.
- **`remove_disconnected_chunks.py`**: Removes text chunks that are disconnected from the main content.
- **`chunk_by_sentence.py`**: Splits text into chunks by sentences.
- **`chunk_by_word.py`**: Splits text into chunks by words.
- **`chunk_by_paragraph.py`**: Splits text into chunks by paragraphs.
- **`query_chunks.py`**: Queries existing chunks for specific content.

---

## **9. Storage Tasks**
Handles indexing and storage of data points and graph edges.

- **`index_data_points.py`**: Indexes data points for efficient retrieval.
- **`index_graph_edges.py`**: Indexes edges within a graph structure.
- **`add_data_points.py`**: Adds new data points to the storage system.

---

## **10. Repository Processing Tasks**
Processes code repositories for dependency graphs and file relationships.

- **`extract_code_parts.py`**: Extracts parts of code for analysis.
- **`get_repo_file_dependencies.py`**: Retrieves file-level dependencies in a repository.
- **`top_down_repo_parse.py`**: Parses repositories from a top-down perspective.
- **`enrich_dependency_graph.py`**: Enriches dependency graphs with additional data.
- **`get_local_dependencies.py`**: Identifies local dependencies in repositories.
- **`expand_dependency_graph.py`**: Expands the scope of dependency graphs.

---

## **11. Document Tasks**
Handles operations related to document processing.

- **`extract_chunks_from_documents.py`**: Extracts text chunks from documents.
- **`classify_documents.py`**: Classifies documents into categories.
- **`check_permissions_on_documents.py`**: Verifies permissions for accessing documents.

---

## Detailed Task Example: Category Extraction

Data enrichment is the process of enhancing raw data with additional information to make it more valuable. This template is a sample task that extracts categories from a document and populates a graph with the extracted categories.

Let's go over the steps to use this template [full code provided here](https://github.com/topoteretes/cognee/blob/main/cognee/tasks/chunk_naive_llm_classifier/chunk_naive_llm_classifier.py):


This function is designed to classify chunks of text using a specified language model. The goal is to categorize the text, map relationships, and store the results in a vector engine and a graph engine. The function is asynchronous, allowing for concurrent execution of tasks like classification and data point creation.

### Parameters

- `data_chunks: list[DocumentChunk]`: A list of text chunks to be classified. Each chunk represents a piece of text and includes metadata like `chunk_id` and `document_id`.
- `classification_model: Type[BaseModel]`: The model used to classify each chunk of text. This model is expected to output labels that categorize the text.

### Steps in the Function

#### Check for Empty Input

```python
if len(data_chunks) == 0:
    return data_chunks
```

If there are no data chunks provided, the function returns immediately with the input list (which is empty).

#### Classify Each Chunk

```python
chunk_classifications = await asyncio.gather(
    *[extract_categories(chunk.text, classification_model) for chunk in data_chunks],
)
```

The function uses `asyncio.gather` to concurrently classify each chunk of text. `extract_categories` is called for each chunk, and the results are collected in `chunk_classifications`.

#### Initialize Data Structures

```python
classification_data_points = []
```

A list is initialized to store the classification data points that will be used later for mapping relationships and storing in the vector engine.

#### Generate UUIDs for Classifications

The function loops through each chunk and generates unique identifiers (UUIDs) for both the main classification type and its subclasses:

```python
classification_data_points.append(uuid5(NAMESPACE_OID, chunk_classification.label.type))
classification_data_points.append(uuid5(NAMESPACE_OID, classification_subclass.value))
```

These UUIDs are used to uniquely identify classifications and ensure consistency.

#### Retrieve or Create Vector Collection

```python
vector_engine = get_vector_engine()
collection_name = "classification"
```

The function interacts with a vector engine. It checks if the collection named "classification" exists. If it does, it retrieves existing data points to avoid duplicates. Otherwise, it creates the collection.

#### Prepare Data Points, Nodes, and Edges

The function then builds a list of `data_points` (representing the classification results) and constructs nodes and edges to represent relationships between chunks and their classifications:

```python
data_points.append(DataPoint[Keyword](...))
nodes.append((...))
edges.append((...))
```

- **Nodes**: Represent classifications (e.g., media type, subtype).
- **Edges**: Represent relationships between chunks and classifications (e.g., "is_media_type", "is_subtype_of").

#### Create Data Points and Relationships

If there are new nodes or edges to add, the function stores the data points in the vector engine and updates the graph engine with the new nodes and edges:

```python
await vector_engine.create_data_points(collection_name, data_points)
await graph_engine.add_nodes(nodes)
await graph_engine.add_edges(edges)
```

#### Return the Processed Chunks

Finally, the function returns the processed `data_chunks`, which can now be used further as needed:

```python
return data_chunks
```

## Additional Notes
- Each task is designed to handle a specific functionality within the system.
- Ensure that dependencies and configurations are properly set up for each task to function as intended.

For further details, refer to the inline documentation within each task file.
````

## File: content/tutorials/load-your-data.mdx
````
---
title: Load your data
---

export function generateMetadata() {
  return {
    title: "Cognee Tutorial - Load your data",
    description: "Learn how to load data into cognee and vizualize the generated knowledge graph.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/tutorials/load-your-data",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/tutorials/load-your-data",
      type: "website",
      title: "Cognee Tutorial - Load your data",
      description: "Learn how to load data into cognee and vizualize the generated knowledge graph.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Tutorial - Load your data",
      description: "Learn how to load data into cognee and vizualize the generated knowledge graph.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


# Load your data

**Difficulty**: Beginner

## Overview


cognee let's you load from 30+ data sources using dlt. You can connect relational, graph and vector stores to cognee.

#### Let's create a basic LLM memory with cognee

Adding data to our graph and connecting it to LLM can help LLM reason better.
You move from large amounts of text to structured data. See before and after bellow.

Here is what we start with:

![Before ](/images/cognee_raw_text_example.png)

And here is how it ends:

![After ](/images/cognee_graph_example.png)

<details>
  <summary>Step 1: Clone cognee repo</summary>
      ```
    git clone https://github.com/topoteretes/cognee.git
    ```
    And our getting started repo
        ```
    git clone https://github.com/topoteretes/cognee-starter.git
        ```

</details>
<details>
  <summary>Step 2: Install with poetry</summary>

  Navigate to cognee repo
  ```
  cd cognee
  ```
  Install with poetry
  ```
  poetry install
  ```
</details>
<details>
  <summary>Step 3: Run simple cognee script </summary>
    Create a python file called simple_example.py
    and copy the  code from the following link into it

    https://github.com/topoteretes/cognee-starter/blob/main/src/pipelines/default.py
</details>

<details>
  <summary>Step 4: Run cognee </summary>
  In order to load the data
  Run
  ```
  python simple_example.py
  ```

</details>

<details>
  <summary>Step 5: Inspect your cognee graph  </summary>
  The script will create an html file in the root folder that you can inspect and check the graph
      ```
import webbrowser
import os
from cognee.api.v1.visualize.visualize import visualize_graph
await visualize_graph()
home_dir = os.path.expanduser("~")
html_file = os.path.join(home_dir, "graph-visualization.html")
webbrowser.open(f"file://{html_file}")
# display(html_file) in notebook 
        ```
</details>

If you prefer video tutorial, check this short video that our engineer Igor made

<iframe
  width="600"
  height="340"
  src="https://www.youtube.com/embed/1bezuvLwJmw"
  title="cognee base introduction video"
  frameBorder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowFullScreen
></iframe>


#### Join the Conversation!
Have questions? Join our community now to connect with professionals, share insights, and get your questions answered!
<br></br>
  <a href="https://discord.gg/m63hxKsp4p" target="_blank" rel="noopener noreferrer">
    <button className="button cta-button">
      Join the community
    </button>
  </a>
````

## File: content/tutorials/turn-your-repo-into-graph.mdx
````
---
title: Turn your repo into graph
---

export function generateMetadata() {
  return {
    title: "Cognee Tutorial - Turn your repo into graph",
    description: "Learn how to ingest a codebase using our codegraph pipeline, analyze the results and run code-based search.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/tutorials/turn-your-repo-into-graph",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/tutorials/turn-your-repo-into-graph",
      type: "website",
      title: "Cognee Tutorial - Turn your repo into graph",
      description: "Learn how to ingest a codebase using our codegraph pipeline, analyze the results and run code-based search.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Tutorial - Turn your repo into graph",
      description: "Learn how to ingest a codebase using our codegraph pipeline, analyze the results and run code-based search.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


# Turn your repo into graph

**Difficulty**: Beginner

## Overview

Cognee offers a simple way to build a **code graph** from your Python projects. Once generated, this graph makes it easier to navigate and query your code.

<br/>
<button><a href="https://colab.research.google.com/drive/1ByJshVC1h6Unn4bdVHUfr0JCNHbd0rFe#scrollTo=5aVmMId12Hzj"><img src="" heght="15px"/><img
  src="https://colab.research.google.com/assets/colab-badge.svg"
  alt="open with Colab" width="150px"/></a></button>


Below, you'll learn how to install cognee, analyze a codebase using a code graph pipeline, and run a code-based search query in just a few easy steps. 

Here is a quick-start guide.

<details>
  <summary>Step 1: Install cognee</summary>

    ```bash
    pip install cognee[codegraph]
    ```
  We begin by installing the `cognee[codegraph]` package, which contains all the dependencies for generating and analyzing code graphs.
</details>
<details>
  <summary>Step 2: Set Environment Variables</summary>
  ```bash
	import os
	os.environ["LLM_API_KEY"] = "sk-"  # Replace with your actual API key
  ```
  Remember to replace "sk-" with your actual key before running the notebook. Here's a guide on how to get your [OpenAI API key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key).

  In case you want to use another provider, please set the env variables. See an example for Mistral [here](https://discord.com/channels/1120795297094832337/1120795297094832340/1340407247582269533).
</details>
<details>
  <summary>Step 3: Clone a Repo to Analyze</summary>
  ```
  git clone https://github.com/hande-k/simple-repo.git # Replace it with your preferred repo
  repo_path = "/{path-to-your-repo}/simple-repo" 
  ```
  This sample repo will be used by cognee to build a code graph. Adjust `repo_path` if you clone to a different location.

</details>
<details>
  <summary>Step 4: Create & Run the Code Graph Pipeline</summary>

  ```python
  import cognee
  from cognee.api.v1.cognify.code_graph_pipeline import run_code_graph_pipeline

  async def codify(repo_path: str):
      print("\nStarting code graph pipeline...")
      async for result in run_code_graph_pipeline(repo_path, False):
          print(result)
      print("\nPipeline completed!")
  ```

  ```python
  await codify(repo_path)
  ```

  Running this pipeline analyzes the code in the repo and constructs an internal graph representation for quick navigation and searching.

</details>
<details>
  <summary>Step 5: Set Up Summarization Prompt</summary>
  
  ```python
    with open("summarize_search_results.txt", "w") as f:
    f.write(
        "You are a helpful assistant that understands the given user query "
        "and the results returned based on the query. Provide a concise, "
        "short, to-the-point user-friendly explanation based on these."
    )

  ```

  We create a text file containing a system prompt. The language model will use this prompt to summarize search results.

</details>
<details>
  <summary>Step 6: A Helper Function for Search & Summary</summary>
  
  
 ```python
  from cognee.modules.search.types import SearchType
  from cognee.infrastructure.llm.prompts import read_query_prompt
  from cognee.infrastructure.llm.get_llm_client import get_llm_client

  async def retrieve_and_generate_answer(query: str) -> str:
      search_results = await cognee.search(query_type=SearchType.CODE, query_text=query)
      prompt_path = "/content/summarize_search_results.txt"
      system_prompt = read_query_prompt(prompt_path)
      llm_client = get_llm_client()

      answer = await llm_client.acreate_structured_output(
          text_input = (
              f"Search Results:\n{str(search_results)}\n\n"
              f"User Query:\n{query}\n"
          ),
          system_prompt=system_prompt,
          response_model=str,
      )
      return answer

  ``` 
 
  With this function, cognee retrieves code-based search results for a user query, and the language model converts them into a concise explanation.

</details>
<details>
  <summary>Step 7: Run a Sample Query</summary>
    ```
    user_query = "add_your_query" # Replace it with your query
    answer = await retrieve_and_generate_answer(user_query)
    print("===== ANSWER =====")
    print(answer)
    ```
    
    
   Cognee uses its code graph to find relevant references, and the language model produces a short, user-friendly answer.

</details>

We hope this quick walkthrough helps you get started with cognee’s code graph and search capabilities. Experiment with different codebases and queries to see the full power of cognee in action!

### Join the Conversation!

Have questions or need more help? Join our community to connect with professionals, share insights, and get your questions answered!
<br></br>
<a href="https://discord.gg/m63hxKsp4p" target="_blank" rel="noopener noreferrer">
<button className="button cta-button">
Join the community
</button>
</a>
````

## File: content/tutorials/use-ontology.mdx
````
---
title: Use Ontologies
---

export function generateMetadata() {
  return {
    title: "Cognee Tutorial - Use Ontologies",
    description: "Learn how to define a custom ontologies and build a knowledge graph that adheres to it.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/tutorials/use-ontology",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/tutorials/use-ontology",
      type: "website",
      title: "Cognee Tutorial - Use Ontologies",
      description: "Learn how to define a custom ontologies and build a knowledge graph that adheres to it.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Tutorial - Use Ontologies",
      description: "Learn how to define a custom ontologies and build a knowledge graph that adheres to it.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


# Use Ontologies

**Difficulty**: Easy

## Overview

In this tutorial, you'll learn how to build a knowledge graph using the cognee framework together with your own custom ontology. We’ll guide you through adding text data, integrating an OWL-based ontology to enrich your graph, and querying for insights.

By the end, you will have:

- Added raw text data representing information about car manufacturers and technology companies.
- Integrated a custom ontology (OWL file) that defines semantic relationships.
- Run the cognee pipeline to generate and inspect your knowledge graph.
- Queried the graph to extract specific insights.

What You'll Learn

- Environment Setup: Installing cognee and preparing your workspace.
- Data Ingestion: Adding raw text data for processing.
- Ontology Integration: Using a custom ontology to structure your data.
- Graph Creation: Running the pipeline to build your knowledge graph.
- Query & Visualization: Searching the graph and visualizing the results.

<details>
  <summary>Step 1: Install cognee with poetry</summary>

  Navigate to cognee repo
  ```
  cd cognee
  ```
  Install with poetry
  ```
  poetry install
  ```

</details>
<details>
  <summary>Step 2: Create a Python script that includes your text data.</summary>
  
For example, you can define two text blocks as follows:

  ```python
text_1 ='''
1. Audi
Audi is known for its modern designs and advanced technology. Founded in the early 1900s, the brand has earned a reputation for precision engineering and innovation. With features like the Quattro all-wheel-drive system, Audi offers a range of vehicles from stylish sedans to high-performance sports cars.

2. BMW
BMW, short for Bayerische Motoren Werke, is celebrated for its focus on performance and driving pleasure. The company’s vehicles are designed to provide a dynamic and engaging driving experience, and their slogan, "The Ultimate Driving Machine," reflects that commitment. BMW produces a variety of cars that combine luxury with sporty performance.

3. Mercedes-Benz
Mercedes-Benz is synonymous with luxury and quality. With a history dating back to the early 20th century, the brand is known for its elegant designs, innovative safety features, and high-quality engineering. Mercedes-Benz manufactures not only luxury sedans but also SUVs, sports cars, and commercial vehicles, catering to a wide range of needs.

4. Porsche
Porsche is a name that stands for high-performance sports cars. Founded in 1931, the brand has become famous for models like the iconic Porsche 911. Porsche cars are celebrated for their speed, precision, and distinctive design, appealing to car enthusiasts who value both performance and style.

5. Volkswagen
Volkswagen, which means “people’s car” in German, was established with the idea of making affordable and reliable vehicles accessible to everyone. Over the years, Volkswagen has produced several iconic models, such as the Beetle and the Golf. Today, it remains one of the largest car manufacturers in the world, offering a wide range of vehicles that balance practicality with quality.
'''

text_2 = '''
1. Apple
Apple is renowned for its innovative consumer electronics and software. Its product lineup includes the iPhone, iPad, Mac computers, and wearables like the Apple Watch. Known for its emphasis on sleek design and user-friendly interfaces, Apple has built a loyal customer base and created a seamless ecosystem that integrates hardware, software, and services.

2. Google
Founded in 1998, Google started as a search engine and quickly became the go-to resource for finding information online. Over the years, the company has diversified its offerings to include digital advertising, cloud computing, mobile operating systems (Android), and various web services like Gmail and Google Maps. Google’s innovations have played a major role in shaping the internet landscape.

3. Microsoft
Microsoft Corporation has been a dominant force in software for decades. Its Windows operating system and Microsoft Office suite are staples in both business and personal computing. In recent years, Microsoft has expanded into cloud computing with Azure, gaming with the Xbox platform, and even hardware through products like the Surface line. This evolution has helped the company maintain its relevance in a rapidly changing tech world.

4. Amazon
What began as an online bookstore has grown into one of the largest e-commerce platforms globally. Amazon is known for its vast online marketplace, but its influence extends far beyond retail. With Amazon Web Services (AWS), the company has become a leader in cloud computing, offering robust solutions that power websites, applications, and businesses around the world. Amazon’s constant drive for innovation continues to reshape both retail and technology sectors.

5. Meta
Meta, originally known as Facebook, revolutionized social media by connecting billions of people worldwide. Beyond its core social networking service, Meta is investing in the next generation of digital experiences through virtual and augmented reality technologies, with projects like Oculus. The company’s efforts signal a commitment to evolving digital interaction and building the metaverse—a shared virtual space where users can connect and collaborate.
'''
```
</details>
<details>
  <summary>Step 3: Create Your Custom Ontology</summary>

([**Ontology file example**](https://github.com/topoteretes/cognee/blob/dev/examples/python/ontology_input_example/basic_ontology.owl))

```xml
<?xml version="1.0" encoding="UTF-8"?>
        <rdf:RDF
           xmlns:ns1="http://example.org/ontology#"
           xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
           xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
        >
          <rdf:Description rdf:about="http://example.org/ontology#Volkswagen">
            <rdfs:comment>Created for making cars accessible to everyone.</rdfs:comment>
            <ns1:produces rdf:resource="http://example.org/ontology#VW_Golf"/>
            <ns1:produces rdf:resource="http://example.org/ontology#VW_ID4"/>
            <ns1:produces rdf:resource="http://example.org/ontology#VW_Touareg"/>
            <rdf:type rdf:resource="http://example.org/ontology#CarManufacturer"/>
            <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#NamedIndividual"/>
          </rdf:Description>
          <!-- Additional ontology definitions follow -->
        </rdf:RDF>
```
</details>        
<details>
  <summary>Step 4: Create a python script and include the following code</summary>

You can find a fully working demo in the following link:
([**Ontology demo example**](https://github.com/topoteretes/cognee/blob/dev/examples/python/ontology_demo_example.py))

```python
import cognee
import asyncio
import logging
import os

from cognee.api.v1.search import SearchType
from cognee.api.v1.visualize.visualize import visualize_graph
from cognee.shared.utils import setup_logging

# Define your text data (insert your full texts for text_1 and text_2)
text_1 = """insert full text_1 here"""
text_2 = """insert full text_2 here"""

async def main():
    # Step 1: Reset data and system state
    await cognee.prune.prune_data()
    await cognee.prune.prune_system(metadata=True)

    # Step 2: Add text data
    text_list = [text_1, text_2]
    await cognee.add(text_list)

    # Step 3: Create knowledge graph using the custom ontology
    ontology_path = os.path.join(
        os.path.dirname(os.path.abspath(__name__)), "ontology_input_example/basic_ontology.owl"
    )
    pipeline_run = await cognee.cognify(ontology_file_path=ontology_path)
    print("Knowledge with ontology created.")

    # Step 4: Calculate descriptive metrics
    await cognee.get_pipeline_run_metrics(pipeline_run, include_optional=True)
    print("Descriptive graph metrics saved to database.")

    # Step 5: Query insights from the graph
    search_results = await cognee.search(
        query_type=SearchType.GRAPH_COMPLETION,
        query_text="What are the exact cars and their types produced by Audi?",
    )
    print(search_results)

    # Step 6: Visualize the knowledge graph and save it to HTML
    await visualize_graph()

if __name__ == "__main__":
    setup_logging(logging.INFO)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main())
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
```
This script will:

- Reset any previous data.
- Add your text data to the system.
- Use your custom ontology to create a semantically enriched graph.
- Calculate graph metrics.
- Query the graph for insights.
- Visualize the graph.

</details>
<details>
  <summary>Step 5: Execute your script from the terminal</summary>

```
python your_script.py
```
</details>

## Summary

In this tutorial, you learned how to:

- Set Up: Install cognee and prepare your environment.
- Add Data: Ingest raw text data about car manufacturers and technology companies.
- Integrate an Ontology: Use a custom OWL ontology to define relationships.
- Build the Graph: Run the pipeline to generate a knowledge graph.
- Query & Visualize: Retrieve specific insights and visualize the graph.

This method not only helps you organize complex data but also leverages semantic relationships to enhance your data insights.
````

## File: content/tutorials/use-the-api.mdx
````
---
title: Use the API
---

export function generateMetadata() {
  return {
    title: "Cognee Tutorial - Use the API",
    description: "Learn how to start the cognee API, authenticate and call available API routes.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/tutorials/use-the-api",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/tutorials/use-the-api",
      type: "website",
      title: "Cognee Tutorial - Use the API",
      description: "Learn how to start the cognee API, authenticate and call available API routes.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Tutorial - Use the API",
      description: "Learn how to start the cognee API, authenticate and call available API routes.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


# Use the API

**Difficulty**: Medium

## Overview

This tutorial demonstrates how to interact with cognee's API service using Docker and cURL. The API allows you to:
- **Set up** your environment with an API key
- **Start** the API service using Docker
- **Authenticate** to get an access token
- **Upload** a document (in this case, a text file containing *Alice in Wonderland*)
- **Process** the document with cognee's pipeline
- **Search** the processed content with natural language queries

---

## Step 1: Environment Setup

First, create a `.env` file that contains your API key. This key is used by the underlying language model (LLM) that powers cognee.

```bash
echo 'LLM_API_KEY="YOUR-KEY"' > .env
```

*This step ensures that cognee can access your LLM credentials.*

---

## Step 2: Starting the API Service

Pull and run the cognee Docker container:

```bash
docker pull cognee/cognee:main
docker run -d -p 8000:8000 --name cognee_container -v $(pwd)/.env:/app/.env cognee/cognee:main
```

*This command pulls the latest cognee image and starts it with your environment file mounted.*

---

## Step 3: Authentication

Obtain an access token using the default credentials:

```bash
access_token=$(curl --location 'http://127.0.0.1:8000/api/v1/auth/login' \
  --form 'username="default_user@example.com"' \
  --form 'password="default_password"' | sed -n 's/.*"access_token":"\([^"]*\)".*/\1/p')

echo "Access Token: $access_token"
```

*The access token will be used to authenticate all subsequent API requests.*

---

## Step 4: Uploading the Document

Upload Alice in Wonderland to a dataset called 'test-dataset':

```bash
curl --location 'http://127.0.0.1:8000/api/v1/add' \
  --header "Authorization: Bearer $access_token" \
  --form 'data=@"/Users/soobrosa/github/cognee/examples/data/alice_in_wonderland.txt"' \
  --form 'datasetId="test-dataset"'
```

*This uploads the document and associates it with the specified dataset ID.*

---

## Step 5: Processing the Document

Process the uploaded dataset:

```bash
curl --location 'http://127.0.0.1:8000/api/v1/cognify' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $access_token" \
--data '{
 "datasets": ["test-dataset"]
}'
```

*This step processes the document through cognee's pipeline, preparing it for querying.*

---

## Step 6: Performing Search Queries

Now you can query the processed dataset. Here are three example queries using the COMPLETION search type:

### Query 1: List Important Characters

```bash
curl --location 'http://127.0.0.1:8000/api/v1/search' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $access_token" \
--data '{
 "searchType": "COMPLETION",
 "query": "List me all the important characters in Alice in Wonderland."
}'
```

### Query 2: How Did Alice End Up in Wonderland?

```bash
curl --location 'http://127.0.0.1:8000/api/v1/search' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $access_token" \
--data '{
 "searchType": "COMPLETION",
 "query": "How did Alice end up in Wonderland?"
}'
```

### Query 3: Describe Alice's Personality

```bash
curl --location 'http://127.0.0.1:8000/api/v1/search' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer $access_token" \
--data '{
 "searchType": "COMPLETION",
 "query": "Tell me about Alice'\''s personality."
}'
```

---

## Conclusion

This tutorial showed you how to use cognee's API to:
- Set up your environment
- Start the cognee service using Docker
- Authenticate and get an access token
- Upload and process a document
- Query the processed content using natural language

You can adapt these steps for your own use cases, whether you're building a search application, a knowledge base, or any other system that needs powerful document processing and querying capabilities.

Happy coding!
````

## File: content/tutorials/user-authentication.mdx
````
---
title: User Authentication
---

export function generateMetadata() {
  return {
    title: "Cognee Tutorial - User Authentication",
    description: "Authenticate users in cognee. Use third-party auth providers with cognee.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/tutorials/user-authentication",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/tutorials/user-authentication",
      type: "website",
      title: "Cognee Tutorial - User Authentication",
      description: "Authenticate users in cognee. Use third-party auth providers with cognee.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Tutorial - User Authentication",
      description: "Authenticate users in cognee. Use third-party auth providers with cognee.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


# User Authentication in Cognee

This document explains how user authentication functions in the Cognee backend in two distinct scenarios:

1. When user authentication and authorization is handled by Cognee
2. When Cognee is used as a third-party library and only uses bearer tokens generated with get_token.py to authenticate user requests

## 1. Authentication Handled by Cognee

### Overview

When Cognee handles authentication, it uses FastAPI Users, a comprehensive authentication system for FastAPI. Cognee implements JWT (JSON Web Token) based authentication with bearer tokens, and supports user registration, login, password reset, and email verification flows.

### Key Components

#### Authentication Backend

The authentication system is built around the `AuthenticationBackend` class from FastAPI Users, with a custom JWT strategy:

- **Bearer Transport**: Used for transmitting tokens in the `Authorization` header
- **JWT Strategy**: Customized to include user ID, tenant ID, and roles in the token payload
- **Token Lifetime**: Default is 1 hour (3600 seconds)

#### User Management

User management is handled through the `UserManager` class, which provides:

- User registration
- Password management (reset, change)
- Email verification
- User retrieval and validation
- Custom post-registration hooks

#### Database Integration

Users are stored in a relational database, accessed through SQLAlchemy:

- User model includes email, password (hashed), tenant association, roles, and status flags
- User data is retrieved using async database sessions

### Authentication Flow

#### Registration

1. User submits registration data (email, password) to `/api/v1/auth/register`
2. The system validates the data and checks for existing users
3. If valid, a new user is created with the provided details
4. The password is securely hashed before storage
5. Optional email verification can be enabled

#### Login

1. User submits credentials to `/api/v1/auth/jwt/login`
2. The system validates the credentials against the stored user data
3. If valid, a JWT token is generated with user information (user_id, tenant_id, roles)
4. The token is returned to the client for use in subsequent requests

#### Authentication on API Requests

1. Client includes the token in the `Authorization` header as `Bearer {token}`
2. The system extracts and validates the token on protected endpoints
3. The user information is extracted from the token and made available to the endpoint
4. Role-based access control can be implemented based on the roles in the token

### Security Features

- Password hashing for secure storage
- Token expiration (1 hour by default)
- JWT signature validation to prevent tampering
- Protection against common attacks (CSRF, XSS)
- Role-based access control

### Example Usage in API Endpoints

Protected endpoints use the `get_authenticated_user` dependency to require authentication:

```python
@router.post("/", response_model=None)
async def cognify(payload: CognifyPayloadDTO, user: User = Depends(get_authenticated_user)):
    # Access to user.id, user.tenant_id, and user.roles
    # Authenticated endpoint logic here
```

### Frontend Integration

Cognee's frontend stores the JWT token in localStorage and includes it in all API requests:

```typescript
fetch('http://127.0.0.1:8000/api' + url, {
  ...options,
  headers: {
    ...options.headers,
    'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
  },
})
```

## 2. Cognee as a Third-Party Library with Bearer Tokens

### Overview

When Cognee is used as a third-party library, authentication is handled externally, and Cognee only validates bearer tokens generated by the `get_token.py` script. This approach is suitable for integrating Cognee into existing systems with their own authentication mechanisms.

### Token Generation

The `get_token.py` script provides a simple way to generate JWT tokens for authenticating with Cognee:

```python
def create_jwt(user_id: str, tenant_id: str, roles: list[str]):
    payload = {
        "user_id": user_id,
        "tenant_id": tenant_id,
        "roles": roles,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),  # 1 hour expiry
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
```

This function creates a signed JWT with:
- User ID
- Tenant ID
- Roles list
- Expiration time (1 hour from creation)

The token is signed with a secret key, which should be the same as the one used by the Cognee instance (`FASTAPI_USERS_JWT_SECRET` environment variable).

### Authentication Flow

1. **External System**: Handles user authentication through its own mechanisms
2. **Token Generation**: Uses `get_token.py` to create a bearer token with the user's information
3. **API Requests**: Includes the token in the `Authorization` header
4. **Cognee Validation**: Validates the token and extracts user information

### Implementation Steps

1. Import and use the token generation function:
   ```python
   from cognee.get_token import create_jwt
   
   # Generate a token for a user
   token = create_jwt(
       user_id="6763554c-91bd-432c-aba8-d42cd72ed659", 
       tenant_id="tenant_456", 
       roles=["admin"]
   )
   ```

2. Include the token in API requests:
   ```python
   headers = {
       "Authorization": f"Bearer {token}"
   }
   
    response = requests.get("http://{your-cognee-instance}/api/v1/settings",
                         headers=headers)
   ```

### Security Considerations

- Keep the secret key secure and consistent between token generation and Cognee
- Implement proper token expiration handling
- Ensure roles assigned in tokens align with the permissions needed
- Consider implementing token revocation if needed for security purposes

### Custom Token Validation

The token validation in Cognee happens through the `get_authenticated_user` function, which:

1. Extracts the token from the Authorization header
2. Verifies the token signature using the secret key
3. Checks for token expiration
4. Extracts and returns user information from the token payload

If token validation fails, the API returns appropriate HTTP error codes (401 for authentication issues).

## Conclusion

Cognee provides flexible authentication options to suit different deployment scenarios:

1. **Full Authentication Stack**: When used as a standalone system, Cognee provides a complete authentication system with user management, registration, login, and token handling.

2. **Token-Based Integration**: When integrated into existing systems, Cognee can validate bearer tokens generated externally, allowing seamless integration with existing authentication mechanisms.

Both approaches use JWT tokens for secure authentication, with user, tenant, and role information included in the token payload to support authentication and authorization within Cognee's functionality.
````

## File: content/use-cases/chatbots.mdx
````
---
title: Chatbots
---

export function generateMetadata() {
  return {
    title: "Cognee Use Case - Chatbots",
    description: "Personalizing Chatbots with Timeseries. LLM chatbots. LLM chatbot agent.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/use-cases/chatbots",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/use-cases/chatbots",
      type: "website",
      title: "Cognee Use Case - Chatbots",
      description: "Personalizing Chatbots with Timeseries. LLM chatbots. LLM chatbot agent.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Use Case - Chatbots",
      description: "Personalizing Chatbots with Timeseries. LLM chatbots. LLM chatbot agent.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


## Case Study: Personalizing Chatbots with Timeseries, Behaviors, and More

Chatbots powered by LLMs are redefining **customer service**, **internal communication**, and **personalized recommendations** across industries. In financial services, pharma, and even other industries, these chatbots can leverage provide more relevant, customized interactions - beyond direct Text-to-SQL querying.


### Scenario: An Investment Advisory Chatbot Assists Clients with Portfolio Decisions

- Uses **time-series data** to identify spending patterns.
- Leverages **user behavior** to suggest savings plans.
- Integrates **business logic** to enforce compliance with financial regulations.

Queries might include:

> *“What’s my portfolio’s performance trend over the last year?”*
> 

> *“Suggest adjustments to reduce volatility while maintaining similar returns.”*
>

### Challenges:
- **Dynamic Personalization:** Each user’s investment history, risk profile, and interactions form a personal data layer.
- **Temporal Data Understanding:** Time-series analysis is needed to interpret trends, volatility shifts, and performance changes over specific periods.
- **Multi-Modal Context:** The chatbot should integrate behavior analytics, market conditions, and portfolio constraints into a cohesive response.

### Solution:
**Knowledge Graphs (KG) & Contextualization:**
By building a KG enriched with user segments, product categories, and historic interaction patterns, the LLM can provide responses rooted in the individual’s context. When paired with Text-to-SQL capabilities, it can surface data-driven recommendations, filtering queries through the lens of each user’s unique financial journey or, in the case of pharma, clinical patterns relevant to individual practitioners or researchers.


Read more about our approach in our [blog](https://www.cognee.ai/blog/case-studies/cognee-case-study-with-dynamo) where we achieved a great improvement.

![chatbots_eval_example_dynamo](/images/chatbots_eval_example_dynamo.png)

### A simple example with cognee

![chatbot_code_example](/images/chatbots_code_example.png)

#### Run a Demo Yourself!
Curious about how this works with cognee? Try it out in our notebook [here](https://github.com/topoteretes/cognee/blob/291f1c5a55abacdef3356fabd37ee0a677db34e1/notebooks/cognee_demo.ipynb).

#### Join the Conversation!
Have questions? Join our community now to connect with professionals, share insights, and get your questions answered!
<br></br>
  <a href="https://discord.gg/m63hxKsp4p" target="_blank" rel="noopener noreferrer">
    <button className="button cta-button">
      Join the community
    </button>
  </a>
````

## File: content/use-cases/code-assistants.mdx
````
---
title: Code Assistants
---

export function generateMetadata() {
  return {
    title: "Cognee Use Case - Code Assistants",
    description: "Enhance codebase understanding with graphs and LLMs. Use cognee as a code assistant.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/use-cases/code-assistants",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/use-cases/code-assistants",
      type: "website",
      title: "Cognee Use Case - Code Assistants",
      description: "Enhance codebase understanding with graphs and LLMs. Use cognee as a code assistant.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Use Case - Code Assistants",
      description: "Enhance codebase understanding with graphs and LLMs. Use cognee as a code assistant.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


## CodeGraph: Enhancing Codebase Understanding with Graphs and LLMs

### Scenario:
Modern software development often involves massive codebases spread across multiple repositories, teams, and services. Engineers and AI-based coding copilots struggle to maintain a clear mental model of how components interrelate. For instance:

- **Large Repositories:** A large software project might have a large of GitHub repository, containing thousands of files.
- **Complex Dependencies:** Services often call each other via APIs, share data models, or rely on specific configuration files. Finding the right function, class, or module can become tedious.
- **Evolving Code:** As code evolves, comments get stale, architectural assumptions shift, and documentation becomes outdated, making it hard for coding copilots to reliably generate correct, context-aware suggestions.

### Challenges:
1. **Fragmented Knowledge:** It’s difficult to piece together the entire dependency graph across the entire repository.
2. **Limited Context for LLMs:** Large Language Models struggle with providing accurate code completions or refactoring suggestions if they lack a broader view of the project’s architecture.
3. **Time Lost:** Developers spend significant time searching through repositories, reading documentation, and attempting to piece together the "big picture" of the codebase.

### Solution: Creating a CodeGraph
A **CodeGraph** is a knowledge graph that models the Python codebase at multiple levels of granularity. It goes beyond just indexing code: it captures entities and relationships within and across repositories.

- **Entities:**
  Functions, classes, modules, services, configuration files, APIs, tests, CI/CD pipelines, and documentation pages.

- **Relationships:**
  Who-calls-what (function call graphs), import dependencies, version histories, code ownership, and semantic links (e.g., "this module implements a particular design pattern" or "this API endpoint is deprecated and replaced by another").

How we constructed a CodeGraph:
- Build chain access direct dependency
- Build init mediated direct dependency
- Define pydantic data structures that describe a single knowledge nodes for all nodes
- Create a knowledge graph
- Write an in-memory retriever that gets the graphs skeletons and extracts triplets

Here is an example graph generated with cognee:
![code_assistants_graph_example](/images/code_assistants_graph_example.png)

Read more about our approach in our [blog](https://www.cognee.ai/blog/deep-dives/repo_to_knowledge_graph).

**Enriching CodeGraph with LLMs:**
To make this knowledge even more actionable, integrate Large Language Models that understand code semantics and developer documentation. The LLM can:

1. **Ingest the Graph:**
   The LLM has access to structured context from the CodeGraph, so when a developer asks, *"Where is the function that parses user inputs for our search engine?"*, the LLM can quickly locate that function by following the graph’s relationships rather than brute-forcing file searches.

2. **Provide Context-Rich Suggestions:**
   When the coding copilot suggests a code snippet, it can reference related modules, highlight deprecations, or warn about known compatibility issues. For example, *"You might want to call `FunctionParseUserInput` from `Utils/InputProcessor.js`. It's used in `SearchEngine.js` and depends on `InputSchema.json`."*

3. **Explain Architectural Decisions:**
   Developers can query the LLM about architectural choices: *"Why does `ServiceD` depend on `ServiceE`?"*. The LLM, using the CodeGraph, responds: *"ServiceD calls `ServiceE`'s authentication endpoint to validate tokens, as documented in `ServiceE/docs/auth.md`."*

4. **Link to Documentation and Commit Histories:**
   The LLM can connect a piece of code to its associated design docs, recent commit messages, or open pull requests. If a developer asks, *"How has `UserProfileAPI.js` changed over the last quarter?"* the LLM can summarize major refactoring steps, point to relevant issues that were closed, and link to architectural decision records.

### Outcomes:
- **Improved Developer Productivity:**
  Instead of wading through multiple repositories, developers get immediate, context-aware guidance, saving countless hours of manual searching and guesswork.

- **More Accurate Code Suggestions:**
  Coding copilots armed with a CodeGraph context deliver more reliable and secure code completions, better refactoring strategies, and insightful recommendations.

- **Evolving with the Codebase:**
  As repositories grow, the CodeGraph and the LLM continuously update. This ensures that as code evolves, the memory and context available to developers—and their automated assistants—stays fresh and relevant.


#### Run a Demo Yourself!
Curious about how this works with cognee? Try it out in our notebook [here](https://github.com/topoteretes/cognee/blob/291f1c5a55abacdef3356fabd37ee0a677db34e1/notebooks/cognee_code_graph_demo.ipynb).

#### Join the Conversation!
Have questions? Join our community now to connect with professionals, share insights, and get your questions answered!
<br></br>
  <a href="https://discord.gg/m63hxKsp4p" target="_blank" rel="noopener noreferrer">
    <button className="button cta-button">
      Join the community
    </button>
  </a>
````

## File: content/use-cases/human-resources.mdx
````
---
title: Human Resources
---

export function generateMetadata() {
  return {
    title: "Cognee Use Case - Human Resources",
    description: "HR and talent management enchanced by cognee.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/use-cases/human-resources",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/use-cases/human-resources",
      type: "website",
      title: "Cognee Use Case - Human Resources",
      description: "HR and talent management enchanced by cognee.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Use Case - Human Resources",
      description: "HR and talent management enchanced by cognee.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}

## HR and Talent Management: Aligning CVs and Job Posts with Entity Resolution

### Scenario:
A large enterprise’s HR team is inundated with job applications. Recruiters need to quickly find the best candidates for specific roles, but the data they must sift through is unstructured and scattered:

- **CVs (Resumes):** Arrive in various formats (PDFs, Word docs, online profiles) and contain a mix of structured (degree names, job titles) and unstructured elements (summaries, personal statements).
- **Job Posts:** Stored in a centralized system, with each role described in terms of required skills, qualifications, and experience. Yet, this system doesn’t consistently align with the language or formats used by applicants on their CVs.
- **Internal Talent Databases:** Contain historical performance data, training records, and skill endorsements for existing employees who might be suitable for open roles.

### Challenges:
1. **Inconsistent Terminology:** A “Business Analyst” role might be titled as “Data Insights Specialist” in a CV, and the required skill “SQL proficiency” might appear as “database querying” or “familiarity with SQL-based tools.”
2. **Entity Resolution Complexity:** Different representations of the same entity (e.g., a skill like “machine learning” vs. “ML engineering,” or a company name spelled differently) need to be unified so recruiters see a clear, accurate view.
3. **Volume and Velocity:** With hundreds or thousands of applicants per role and multiple roles open at once, it’s challenging to quickly identify the right candidates without a reliable way to standardize and query this information.

### Solution with KGs & LLMs:
1. **Building a Knowledge Graph:**
   A KG connects roles, skills, qualifications, and experience levels to one another. For instance:
   - Skills like “SQL,” “Python,” and “Data Visualization” are captured as nodes.
   - Job roles link to these skills, indicating required proficiency levels.
   - Educational qualifications, certifications, and industry experience are recorded similarly.

2. **Entity Resolution for Skills & Titles:**
   Using entity resolution techniques, the system normalizes various mentions of the same skill or title. For example:
   - “SQL experience” in one CV and “database querying” in another CV map to a single “SQL” skill node.
   - Different job titles that effectively mean the same role (e.g., “Data Analyst” and “Junior Data Analyst”) link back to a standard role entity.

3. **LLM-Driven Text-to-SQL Queries:**
   With the KG in place, recruiters can use natural language questions against the structured data:
   - *"Show me candidates applying for the Business Analyst role who have demonstrated SQL proficiency and at least 3 years of experience in data analytics."*

   An LLM translates this into an SQL query that retrieves candidates matching these criteria. The KG ensures that the query understands synonyms and resolves variations in terminology across CVs and job postings.

4. **Explaining Results & Candidate Matching:**
   When presenting results, the system can explain why certain candidates are a good fit—highlighting the linked entities (skills, certifications, job titles) and showing how they map to the job’s requirements. This transparency builds trust and speeds up the selection process.

### Outcomes:
- **Faster Shortlisting:** Recruiters spend less time manually parsing CVs and searching through databases.
- **Better Candidate-Role Alignment:** By unifying entities, the system ensures no qualified candidate goes overlooked due to mismatched terminology or formatting.
- **Scalable & Fair Hiring:** As the organization grows, the approach scales to thousands of roles and applicants, maintaining consistency and potentially reducing bias by focusing on structured, contextually rich data.

In essence, applying LLM-driven Text-to-SQL solutions, powered by a well-structured KG and robust entity resolution, helps HR teams instantly understand candidate profiles in relation to job requirements, saving time, reducing complexity, and improving the quality of hiring decisions.


#### Run a Demo Yourself!
Curious about how this works with cognee? Try it out in our notebook [here](https://github.com/topoteretes/cognee/blob/dev/notebooks/hr_demo.ipynb).

#### Join the Conversation!
Have questions? Join our community now to connect with professionals, share insights, and get your questions answered!
<br></br>
  <a href="https://discord.gg/m63hxKsp4p" target="_blank" rel="noopener noreferrer">
    <button className="button cta-button">
      Join the community
    </button>
  </a>
````

## File: content/core-concepts.mdx
````
export const metadata = {
  asIndexPage: true,
  title: "Cognee - Core Concepts",
  description: "Learn about Cognee architecture. Pipelines and tasks. Data ingestion and chunking. Graph generation and ontology inference.",
  alternates: {
    canonical: "https://www.docs.cognee.ai/core-concepts",
  },

  openGraph: {
    url: "https://www.docs.cognee.ai",
    type: "website",
    title: "Cognee - Core Concepts",
    description: "Learn about Cognee architecture. Pipelines and tasks. Data ingestion and chunking. Graph generation and ontology inference.",
    images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
  },

  twitter: {
    site: "@cognee_",
    card: "summary_large_image",
    title: "Cognee - Core Concepts",
    description: "Learn about Cognee architecture. Pipelines and tasks. Data ingestion and chunking. Graph generation and ontology inference.",
    images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
  },
};

# Core Concepts

What cognee does is not trivial, nor is it rocket surgery.

These fundamental concepts will help you understand how cognee works and how to leverage its capabilities effectively.

We will explain the key components and principles that power cognee's knowledge graph system.

* [Architecture](/core-concepts/architecture) shows cognee's system design, components, and how they work together to create a powerful knowledge graph platform.
* [Pipelines](/core-concepts/pipelines) are the data processing workflows that transform raw information into structured knowledge graphs.
* [Chunking](/core-concepts/chunking) is how cognee breaks down large datasets into manageable pieces for efficient processing and analysis.
* [Data Ingestion](/core-concepts/data-ingestion) can import and process data from various sources to build comprehensive knowledge graphs.
* [Graph Generation](/core-concepts/graph-generation) is the process of creating and maintaining semantic knowledge graphs from your data.
* [Ontologies](/core-concepts/ontologies) structure and organize knowledge in meaningful ways.
* [Data Management (CRUD)](/core-concepts/data-management-crud) shows you how to think about interacting with cognee from an other service.
````

## File: content/how-to-guides.mdx
````
---
title: How-to Guides
asIndexPage: true
---

export function generateMetadata() {
  return {
    title: "Cognee - How-to Guides",
    description: "Follow the guide to deploy cognee, visualize graph. Optimize the cognee pipeline. Run cognee with custom models.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/how-to-guides",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/how-to-guides",
      type: "website",
      title: "Cognee - How-to Guides",
      description: "Follow the guide to deploy cognee, visualize graph. Optimize the cognee pipeline. Run cognee with custom models.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee - How-to Guides",
      description: "Follow the guide to deploy cognee, visualize graph. Optimize the cognee pipeline. Run cognee with custom models.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}

# How-to Guides

What you want to do with cognee is up to you, and we're here to help.

These practical guides will help you accomplish specific tasks and customize cognee to your needs.

We will walk through common scenarios and solutions that you'll encounter while working with cognee.

* [Deployment](/how-to-guides/deployment) shows you how to get cognee up and running in your environment.
* [Graph Visualization](/how-to-guides/graph-visualization) helps you explore and understand your knowledge graphs visually.
* [Search Guide](/how-to-guides/search) teaches you how to effectively query and retrieve information from your graphs.
* [Optimization](/how-to-guides/optimization) covers techniques like [Descriptive Metrics](/how-to-guides/optimization/descriptive-metrics) and the [Evaluation Framework](/how-to-guides/optimization/evaluation-framework) to improve performance.
* [Configuration](/how-to-guides/configuration) explains how to customize cognee settings for your specific needs.
* [Remote Models](/how-to-guides/remote-models) shows you how to integrate cloud-based AI models.
* [Local Models](/how-to-guides/local-models) guides you through setting up and using models on your own infrastructure.
* [Cognee Tasks](/how-to-guides/cognee-tasks) walks through common operations and workflows.
* [Own Data Model](/how-to-guides/own-data-model) helps you create and integrate custom data structures.
````

## File: content/index.mdx
````
export async function generateMetadata() {
  return {
    title: "Cognee Documentation - Introduction",
    description: "Learn about Cognee. Take a deep dive into Cognee documentation. Core concepts of Cognee, how-to guides, use cases.",
    alternates: {
      canonical: "https://www.docs.cognee.ai",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai",
      type: "website",
      title: "Cognee Documentation - Introduction",
      description: "Learn about Cognee. Take a deep dive into Cognee documentation. Core concepts of Cognee, how-to guides, use cases.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Documentation - Introduction",
      description: "Learn about Cognee. Take a deep dive into Cognee documentation. Core concepts of Cognee, how-to guides, use cases.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  }
}

import Link from "next/link";
import Image from "next/image";
import DisableToC from "../ui/components/DisableToC";
import ResponsiveImage from "../ui/components/ResponsiveImage";
import Head from "next/head";

<DisableToC />

# Organise your data and get better responses from AI

Your data is like a haystack. The more you have, the harder it is to use it effectively.<br/>
Sending large amounts of data to AI agents can lead to bloat and hallucinations.<br/>
Cognee connects data points and establishes ground truths to improve the accuracy of your AI agents and LLMs.<br/>
Improve the accuracy of your AI agents with Cognee. Connect the dots, find the needle.

* Jump on a [Quickstart](/quickstart) to get cognee running
* Follow a few [Tutorials](/tutorials) to try different use cases easily
* [Core Concepts](/core-concepts) can help you gain a deeper understanding on the inner workings of the system
* [How-to Guides](/how-to-guides) provide you more patterns for advanced usage from technical and functional perspective
* [Use Cases](/use-cases) show the business value you can gain from cognee
* [Integrations](/integrations) show you how to use cognee for Python code analysis with your IDE
* [Reference](/reference) will get you covered with technical details
* Browse [Research](/research) if you want to understand the academic background
* [Resources](/resources) will help you from a beginner, an intermediate and an advanced perspective

<br></br>
<a href="https://discord.gg/m63hxKsp4p" target="_blank" rel="noopener noreferrer">
  <button className="button cta-button">
    Join the conversation!
  </button>
</a>
````

## File: content/integrations.mdx
````
---
title: Integrations
asIndexPage: true
---

export function generateMetadata() {
  return {
    title: "Cognee Integrations",
    description: "Integrate cognee with Cline. Integrate cognee with Continue. Integrate cognee with Roo.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/integrations",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/integrations",
      type: "website",
      title: "Cognee Integrations",
      description: "Integrate cognee with Cline. Integrate cognee with Continue. Integrate cognee with Roo.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Integrations",
      description: "Integrate cognee with Cline. Integrate cognee with Continue. Integrate cognee with Roo.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


# Use cognee to interact with your Python codebase

Try it out with VSCode using
* [Cline](integrations/cline.mdx),
* [Continue](integrations/continue.mdx)
* or [Roo Code](integrations/roo-code.mdx).

You can also use it with [Cursor](integrations/cursor.mdx).
````

## File: content/quickstart.mdx
````
export const metadata = {
  title: "Cognee Docs - Quickstart",
  description: "Prerequisites for running cognee. Cognee installation. Basic usage of cognee. Add data to knowledge graph. Search the knowledge graph.",
  alternates: {
    canonical: "https://www.docs.cognee.ai/quickstart",
  },

  openGraph: {
    url: "https://www.docs.cognee.ai/quickstart",
    type: "website",
    title: "Cognee Docs - Quickstart",
    description: "Prerequisites for running cognee. Cognee installation. Basic usage of cognee. Add data to knowledge graph. Search the knowledge graph.",
    images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
  },

  twitter: {
    site: "@cognee_",
    card: "summary_large_image",
    title: "Cognee Docs - Quickstart",
    description: "Prerequisites for running cognee. Cognee installation. Basic usage of cognee. Add data to knowledge graph. Search the knowledge graph.",
    images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
  },
}

# QUICKSTART

This guide will help you get started with Cognee quickly and efficiently. Follow these step-by-step instructions to set up your environment, install Cognee, and run your first knowledge graph operations.

## Prerequisites

- **Python**: Cognee supports Python versions 3.9 to 3.12
- **Database**: SQLite (default) or PostgreSQL
- **API Key**: OpenAI API key (or alternatives like Ollama or Anyscale)

## 1. Installation

You can install Cognee using either pip or poetry:

### Option A: Using pip (Recommended for beginners)

```bash
pip install cognee
# If you plan to use PostgreSQL
pip install cognee[pg]
```

### Option B: Using Poetry

```bash
# Install Poetry if you don't have it
pip install poetry

# Configure Poetry
poetry config virtualenvs.in-project true
poetry self add poetry-plugin-shell

# Create a new project or navigate to your existing project
# Initialize a new Poetry project if needed
poetry init

# Add Cognee
poetry add cognee
# If you plan to use PostgreSQL
poetry add cognee[pg]

# Activate the virtual environment
poetry shell
```

## 2. Configure Your Environment

### Set up your LLM API key

```python
import os

# Option 1: Set environment variable
os.environ["LLM_API_KEY"] = "YOUR_OPENAI_API_KEY"

# Option 2: Set directly in Cognee config
import cognee
cognee.config.llm_api_key = "YOUR_OPENAI_API_KEY"
```

### Database Configuration (Optional)

By default, Cognee uses SQLite. If you want to use PostgreSQL:

```bash
# Run PostgreSQL in Docker (optional)
docker compose up postgres

# Configure database in your code
import cognee
cognee.config.db_provider = "postgres"  # or "sqlite" (default)
cognee.config.db_connection_string = "postgresql://user:password@localhost:5432/cognee"
```

## 3. Basic Usage

Cognee is asynchronous by design, so you'll need to use `async/await` patterns:

```python
import cognee
import asyncio
from cognee.modules.search.types import SearchType

async def main():
    # Create a clean slate - reset data and system state
    await cognee.prune.prune_data()
    await cognee.prune.prune_system(metadata=True)
    
    # Add content to Cognee
    text = """
    Natural language processing (NLP) is an interdisciplinary
    subfield of computer science and information retrieval.
    """
    
    print("Adding text to cognee:")
    print(text.strip())
    
    # Add the text to make it available for cognify
    await cognee.add(text)
    
    # Process with LLMs to create the knowledge graph
    await cognee.cognify()
    print("Cognify process complete.\n")
    
    # Search the knowledge graph
    query_text = "Tell me about NLP"
    print(f"Searching cognee for insights with query: '{query_text}'")
    
    search_results = await cognee.search(
        query_text=query_text, 
        query_type=SearchType.INSIGHTS
    )
    
    print("Search results:")
    for result_text in search_results:
        print(result_text)

if __name__ == '__main__':
    asyncio.run(main())
```

## 4. Adding Different Types of Content

### Adding Text

```python
await cognee.add("Your text content here")
```

### Adding Files

```python
# Add a file from your filesystem
await cognee.add("file:///path/to/your/document.pdf")
await cognee.add("file:///path/to/your/document.txt")

# Add a file from a URL
await cognee.add("https://example.com/document.pdf")
```



## 5. Working with the Knowledge Graph

### Processing Content

After adding content, you need to process it to create the knowledge graph:

```python
await cognee.cognify()
```

### Searching the Knowledge Graph

Cognee offers multiple search types for different use cases:

```python
from cognee.modules.search.types import SearchType

# Search for insights about relationship between your data points and returns LLM context
results = await cognee.search(
    query_text="Your search query", 
    query_type=SearchType.INSIGHTS
)

# Search for specific information via Graph and provides human readable answer
results = await cognee.search(
    query_text="Your search query", 
    query_type=SearchType.GRAPH_COMPLETION
)

# Search with combination of Graph and Vector store to return a human readable answer
results = await cognee.search(
    query_text="Your search query", 
    query_type=SearchType.COMPLETION
)

# Get summaries of topics and provides that as an answer
results = await cognee.search(
    query_text="Your search query", 
    query_type=SearchType.SUMMARIES
)

# Search for code-related that was processed using codify pipeline that turns Python Github repositories to code
results = await cognee.search(
    query_text="Your search query", 
    query_type=SearchType.CODE
)
```

> **Note:** For a comprehensive reference of all available search types, see the [Search Types Reference](reference/search-types).

### Visualizing the Graph

You can visualize your knowledge graph using the built-in visualization tool:

```python
from cognee.api.v1.visualize.visualize import visualize_graph

# Generate an HTML visualization of your graph
await visualize_graph('./graph-visualization.html')
# The file is saved in your current folder
```

## 6. System Information

### System Folder Location

Cognee stores its system data in a `.cognee_system` folder, typically located:

- When using a virtual environment: Inside your virtual environment directory
- When installed globally: In your user home directory

You can access this folder to view logs, graph visualizations, and other system files.

### Pruning the System

To reset your Cognee instance:

```python
# Reset just the data
await cognee.prune.prune_data()

# Reset system state including metadata
await cognee.prune.prune_system(metadata=True)

# Reset everything
await cognee.prune.prune_all()
```

## 7. Advanced Usage

For more advanced usage, including custom pipelines, check out the [Pipelines documentation](core-concepts/pipelines.md) and [API Reference](reference/api-reference).

## Need Help?

Check out our [starter repo](https://github.com/topoteretes/cognee-starter) for example code and pre-built pipelines.

#### Join the Conversation!
Have questions? Join our community now to connect with professionals, share insights, and get your questions answered!
<br></br>
  <a href="https://discord.gg/m63hxKsp4p" target="_blank" rel="noopener noreferrer">
    <button className="button cta-button">
      Join the community
    </button>
  </a>
````

## File: content/reference.mdx
````
---
title: Reference
asIndexPage: true
---

export function generateMetadata() {
  return {
    title: "Cognee Reference",
    description: "Cognee documentation reference.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/reference",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/reference",
      type: "website",
      title: "Cognee Reference",
      description: "Cognee documentation reference.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Reference",
      description: "Cognee documentation reference.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


# Reference

What you need to know is all here, organized for quick access.

These detailed references provide comprehensive technical information about cognee's components and capabilities.

We have documented everything from infrastructure to evaluation metrics to help you build with confidence.

* [Infrastructure](/reference/infrastructure) details the system architecture, deployment options, and technical requirements.
* [Modules](/reference/modules) documents all core modules and their functionalities in the cognee ecosystem.
* [Tasks](/reference/tasks) provides a complete list of available tasks and their parameters.
* [SDK](/reference/sdk) offers detailed documentation of our software development kit for programmatic access.
* [API](/reference/api-reference) specifies all available endpoints, methods, and response formats.
* [Search Types](/reference/search-types) catalogs the different search mechanisms and their use cases.
* [Descriptive Metrics](/reference/descriptive-metrics) explains all available metrics for system performance analysis.
* [Retriever Evaluation](/reference/retriever-evaluation) documents methods and metrics for evaluating retrieval performance.
* [Colab Notebooks](/reference/colab-notebooks) provides ready-to-use examples and tutorials in notebook format.
* [Ontology Reference](/reference/ontology-reference) details the supported ontology formats and implementation specifications.
````

## File: content/research.mdx
````
---
title: Research
---

export function generateMetadata() {
  return {
    title: "Cognee Research",
    description: "Research collected in the past one year from various sources.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/research",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/research",
      type: "website",
      title: "Cognee Research",
      description: "Research collected in the past one year from various sources.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Research",
      description: "Research collected in the past one year from various sources.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


# Research

The page is dedicated to collecting all research that was collected in the past one year from various sources.

This is not an exhaustive list.

### Research Papers
- [2024/06/04] [Symbolic reasoning](https://arxiv.org/abs/2402.01817)
- [2024/06/04] [Transformers and episodic memory](https://arxiv.org/abs/2405.14992)
- [2024/03/24] [Graph Chain-of-Thought: Augmenting Large Language Models by Reasoning on Graphs](https://arxiv.org/abs/2404.07103)
- [2024/03/24] [Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention](https://arxiv.org/abs/2404.07143)
- [2024/03/24] [Compound AI systems](https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/)
- [2015/07/30] [Multilayer Network of Language](https://arxiv.org/abs/1507.08539)
- [2023/12/12]  [Dense X Retrieval: What Retrieval Granularity Should We Use?](https://arxiv.org/pdf/2312.06648.pdf)
- [2024/01/05] [Retrieval-Augmented Generation for Large Language Models: A Survey](https://arxiv.org/pdf/2312.10997.pdf)
- [2022/10/20]  [Cognitive modelling with multilayer networks: Insights, advancements and future challenges](https://arxiv.org/pdf/2210.00500.pdf)
- [2023/09/20] CoAla framework and relevant literature [literature](https://github.com/ysymyth/awesome-language-agents)
- [2023/06/09] [Mind2Web: Towards a Generalist Agent for the Web](https://arxiv.org/pdf/2306.06070.pdf), Xiang Deng, et al. [[code]](https://github.com/OSU-NLP-Group/Mind2Web) [[demo]](https://osu-nlp-group.github.io/Mind2Web/)
- [2023/06/28] AI Agents in Langchain [https://docs.google.com/presentation/d/1L_CHsg26sDxPmKj285Ob5T2xsAUejBlfiGQSnsSHTk0/edit#slide=id.g254e571859c_0_164](https://docs.google.com/presentation/d/1L_CHsg26sDxPmKj285Ob5T2xsAUejBlfiGQSnsSHTk0/edit#slide=id.g254e571859c_0_164)
- [2023/06/27] Agent infra [https://lilianweng.github.io/posts/2023-06-23-agent/](https://lilianweng.github.io/posts/2023-06-23-agent/)
- [2023/06/05] [Orca: Progressive Learning from Complex Explanation Traces of GPT-4](https://arxiv.org/pdf/2306.02707.pdf), Subhabrata Mukherjee et al.
- [2023/05/25] 📚[Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/pdf/2305.16291.pdf), Guanzhi Wang, et al. [[code]](https://github.com/MineDojo/Voyager) [[website]](https://voyager.minedojo.org/), Shishir G. Patil, et al.
- [2023/05/24] 📚[Gorilla: Gorilla: Large Language Model Connected with Massive APIs](https://arxiv.org/abs/2305.15334)
- [2023/05/17] 📚[Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601), Shunyu Yao, et al.[[code]](https://github.com/kyegomez/tree-of-thoughts) [[code-orig]](https://github.com/ysymyth/tree-of-thought-llm)
- [2023/05/12] 📚[MEGABYTE: Predicting Million-byte Sequences with Multiscale Transformers](https://arxiv.org/abs/2305.07185), Lili Yu, et al.
- [2023/05/09] 📚[FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance](https://arxiv.org/abs/2305.05176), Lingjiao Chen, et al.
- [2023/05/01] 📚[Learning to Reason and Memorize with Self-Notes](https://arxiv.org/abs/2305.00833), Jack Lanchantin, et al.
- [2023/04/24] 📚[WizardLM: Empowering Large Language Models to Follow Complex Instructions](https://arxiv.org/abs/2304.12244), Can Xu, et al.
- [2023/04/22] 📚[LLM+P: Empowering Large Language Models with Optimal Planning Proficiency](https://arxiv.org/abs/2304.11477), Bo Liu, et al.
- [2023/04/07] 📚[Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442), Joon Sung Park, et al. [[code]](https://github.com/mkturkcan/generative-agents)
- [2023/03/30] [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651), Aman Madaan, et al.[[code]](https://github.com/madaan/self-refine)
- [2023/03/30] [HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in HuggingFace](https://arxiv.org/pdf/2303.17580.pdf), Yongliang Shen, et al. [[code]](https://github.com/microsoft/JARVIS) [[demo]](https://huggingface.co/spaces/microsoft/HuggingGPT)
- [2023/03/20] [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/pdf/2303.11366.pdf), Noah Shinn , et al. [[code]](https://github.com/noahshinn024/reflexion)
- [2023/02/23] 📚[Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/abs/2302.12173), Sahar Abdelnab, et al.
- [2023/02/09] 📚[Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/pdf/2302.04761.pdf), Timo Schick, et al. [[code]](https://github.com/lucidrains/toolformer-pytorch)
- [2022/12/12] 📚[LMQL: Prompting Is Programming: A Query Language for Large Language Models](https://arxiv.org/abs/2212.06094), Luca Beurer-Kellner, et al.
- [2022/10/06] [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/pdf/2210.03629.pdf), Shunyu Yao, et al. [[code]](https://github.com/ysymyth/ReAct)
- [2022/07/12] 📚[Inner Monologue: Embodied Reasoning through Planning with Language Models](https://arxiv.org/pdf/2207.05608.pdf), Wenlong Huang, et al. [[demo]](https://innermonologue.github.io/)
- [2022/04/04] [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://github.com/Significant-Gravitas/Nexus/wiki/Awesome-Resources), Michael Ahn, e al. [[demo]](https://say-can.github.io/)
- [2021/12/17] [WebGPT: Browser-assisted question-answering with human feedback](https://arxiv.org/pdf/2112.09332.pdf), Reiichiro Nakano, et al.
- [2021/06/17] 📚[LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685), Edward J. Hu, et al.
- [2023/04/03] [Generative Agents](https://arxiv.org/abs/2304.03442)
- [2023/05/17] [Three of thought: Deliberate Problem Solving with Large Language Mode](https://arxiv.org/abs/2305.10601)ls


### Knowledge Graphs

- [2023/06/09] [Taxonomies: Overview](https://www.brighttalk.com/webcast/9273/605659?utm_source=brighttalk-portal&utm_medium=web&utm_campaign=topic&utm_content=upcoming)

### Blog Articles

- [2023/04/29] [AUTO-GPT: UNLEASHING THE POWER OF AUTONOMOUS AI AGENTS](https://www.leewayhertz.com/autogpt/) By Akash Takyar
- [2023/04/20] [Conscious Machines: Experiments, Theory, and Implementations(Chinese)](https://pattern.swarma.org/article/230) By Jiang Zhang
- [2023/04/18] [Autonomous Agents & Agent Simulations](https://blog.langchain.dev/agents-round/) By Langchain
- [2023/04/16] [4 Autonomous AI Agents you need to know](https://towardsdatascience.com/4-autonomous-ai-agents-you-need-to-know-d612a643fa92) By Sophia Yang
- [2023/03/31] [ChatGPT that learns to use tools](https://zhuanlan.zhihu.com/p/618448188) By Haojie Pan

### Talks

- [2023/06/05] [Two Paths to Intelligence](https://www.youtube.com/watch?v=rGgGOccMEiY&t=1497s) by Geoffrey Hinton
- [2023/05/24] [State of GPT](https://www.youtube.com/watch?v=bZQun8Y4L2A) by Andrej Karpathy | OpenAI
- [2024/03/15] Podcast on AI, Memory by Bill Gurley
````

## File: content/resources.mdx
````
---
title: Resources
---

export function generateMetadata() {
  return {
    title: "Cognee Resources",
    description: "Resources collected so far, demos, videos, images...",
    alternates: {
      canonical: "https://www.docs.cognee.ai/resources",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/resources",
      type: "website",
      title: "Cognee Resources",
      description: "Resources collected so far, demos, videos, images...",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee Resources",
      description: "Resources collected so far, demos, videos, images...",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


# **Resources on Cognee, Semantic Memory, and GraphRAG**

This document provides a structured overview of key resources covering **cognee**, **semantic memory**, and **GraphRAG**, categorized by **beginner, intermediate, and advanced** levels. These resources include documentation, research papers, blog posts, community discussions, and industry reports.

## **📌 Beginner Resources**

### **1. Cognee Documentation**

📄 *Entry point to understand how cognee works with quick tutorials, core concepts, how-to guides, and integration guidelines.*

🔗 [Read here](https://docs.cognee.ai/)

### **2. Sample Use Cases**

📄 *Introduction to real-world examples of how cognee is used.*

🔗 [Read here](https://docs.cognee.ai/use-cases)

### **3. Case Study with Dynamo.fyi**

📝 *A real-life example showcasing how cognee significantly improved answer relevancy.*

🔗 [Read here](https://www.cognee.ai/blog/case-studies/cognee-case-study-with-dynamo)

### **4. Intro to LLM Memory**

📝 *Explaining what AI memory is and how it is used with LLMs.*

🔗 [Read here](https://www.cognee.ai/blog/fundamentals/llm-memory-cognitive-architectures-with-ai)

### **5. AI Memory in Claude Desktop**

🎥 *Showing how cognee is used as a memory system in the Claude Desktop App.*

🔗 [Watch here](https://www.youtube.com/watch?v=fI4hDzguN5k)

### **6. Cognee GraphRAG in 4 Minutes + Visualization**

🎥 *Quick guide to building a GraphRAG solution with cognee.*

🔗 [Watch here](https://www.youtube.com/watch?v=1bezuvLwJmw)

### **7. Interactive Notebooks for Hands-on Learning**

📓 *Hands-on resources for working with cognee’s tasks, building code graphs, and querying with advanced techniques.*

- [Cognee Notebooks Collection](https://docs.cognee.ai/reference/colab-notebooks)
- [Code Graph Pipeline Colab Notebook](https://colab.research.google.com/drive/1ByJshVC1h6Unn4bdVHUfr0JCNHbd0rFe#scrollTo=5aVmMId12Hzj)
- [Demo with Cognee Tasks Colab Notebook](https://colab.research.google.com/drive/1g-Qnx6l_ecHZi0IOw23rg0qC4TYvEvWZ?usp=sharing)
- [Cognee GraphRAG Simple Example](https://colab.research.google.com/drive/18mvLcMi687GNsO7rDoglouW0-QTWNfUz)

---

## **📌 Intermediate Resources**

### **8. Cognitive Architectures for Language Agents**

📝 *Defining cognitive architecture based on an impactful paper (CoALA) and how cognee builds on it.*

🔗 [Read here](https://www.cognee.ai/blog/fundamentals/cognitive-architectures-for-language-agents-explained)

### **9. Cognee GraphRAG**

📝 *Explaining cognee’s GraphRAG approach where it merges graph and vector stores for advanced retrieval and querying.*

🔗 [Read here](https://www.cognee.ai/blog/deep-dives/cognee-graphrag-supercharging-search-with-knowledge-graphs-and-vector-magic)

### **10. Building Knowledge Graphs & Deploying**

🎥 *Explanation of how graphs are connected to LLMs and deployed.*

🔗 [Watch here](https://www.youtube.com/watch?v=86SWVdI5K0Y&t=299s)

### **11. Memory as a Key Component of LLM-Powered Autonomous Agents**

📝 *Developer-friendly yet conceptually rigorous insights into semantic memory and long-term AI memory structures.*

🔗 [Read here](https://lilianweng.github.io/posts/2023-06-23-agent/)

### **12. Microsoft GraphRAG Project**

📚 *Overview of GraphRAG by Microsoft, detailing its benefits and implementation.*

🔗 [Read here](https://www.microsoft.com/en-us/research/project/graphrag/)

### **13. Descriptive Graph Metrics**

🎥 *Exploration of cognee’s graph metrics for evaluating generated knowledge graphs.*

🔗 [Watch here](https://www.youtube.com/watch?v=gNvfdzukd7w&t=190s)

### **14. Cognee Evaluation Framework**

📄 *Overview of how evaluation is structured at cognee, including sample results.*

🔗 [Read here](https://docs.cognee.ai/how-to-guides/optimization/evaluation-framework)

### **15. Community & Industry Discussions on GraphRAG**

💬 *Conversations from Hacker News and Reddit showcasing industry and developer interest in GraphRAG.*

- [Hacker News Discussion on GraphRAG](https://news.ycombinator.com/item?id=40857174)
- [GraphRAG Discussion on Reddit](https://www.reddit.com/r/LangChain/comments/1e66e9r/graphrag/)

---

## **📌 Advanced Resources**

### **16. Knowledge Graphs with Ontology**

📝 *Showing how ontology integration enhances knowledge graphs and their retrieval capabilities.*

🔗 [Read here](https://www.cognee.ai/blog/deep-dives/ontology-ai-memory)

### **17. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**

📄 *The foundational NeurIPS 2020 paper introducing the RAG paradigm.*

🔗 [Read here](https://proceedings.neurips.cc/paper/2020/file/6b493230205f780e1bc26945df7481e5-Paper.pdf)

### **18. From Local to Global: A GraphRAG Approach to Query-Focused Summarization**

📄 *Microsoft’s primary research paper underpinning GraphRAG and its applications.*

🔗 [Read here](https://arxiv.org/html/2404.16130v1)

### **19. Long-Term Memory: The Foundation of AI Self-Evolution**

📄 *Exploring how AI models could develop cognitive abilities and build internal representations.*

🔗 [Read here](https://arxiv.org/pdf/2410.15665)

### **20. Personalized Graph-Based Retrieval for Large Language Models**

📄 *Demonstrates the real-world advantages of graph-based retrieval over purely vector-based solutions.*

🔗 [Read here](https://arxiv.org/pdf/2501.02157)

### **21. Memory, Consciousness, and Large Language Models**

📄 *Proposing a “duality” between Tulving’s theory of human memory and the memory mechanisms of LLMs.*

🔗 [Read here](https://arxiv.org/html/2401.02509v2)

### **22. Hugging Face GraphRAG Paper Collection**

📚 *A collection of research papers on GraphRAG curated by Hugging Face.*

🔗 [Read here](https://huggingface.co/collections/graphrag/graphrag-papers-667566a057208377a1489c82)
````

## File: content/tutorials.mdx
````
export const metadata = {
  asIndexPage: true,
  title: "Cognee Docs - Tutorials",
  description: "Cognee tutorials. Load your data and turn it into a knowledge graph. Create ontologies. Use the cognee API.",
  alternates: {
    canonical: "https://www.docs.cognee.ai/tutorials",
  },

  openGraph: {
    url: "https://www.docs.cognee.ai/tutorials",
    type: "website",
    title: "Cognee Docs - Tutorials",
    description: "Cognee tutorials. Load your data and turn it into a knowledge graph. Create ontologies. Use the cognee API.",
    images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
  },

  twitter: {
    site: "@cognee_",
    card: "summary_large_image",
    title: "Cognee Docs - Tutorials",
    description: "Cognee tutorials. Load your data and turn it into a knowledge graph. Create ontologies. Use the cognee API.",
    images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
  },
}

# Tutorials

These step-by-step guides are lessons to help you get started and make the most of cognee's capabilities.

You will learn about the most important functionality and workflows.

* [Load your data](/tutorials/load-your-data) from 30+ sources into cognee using dlt. Connect relational, graph and vector stores to enhance your LLM's reasoning capabilities.
* [Turn your repo into a graph.](/tutorials/turn-your-repo-into-graph) Extract relationships and insights from the semantic knowledge graph of your codebase structure.
* [Use ontologies](/tutorials/use-ontology) to build knowledge graphs. This tutorial walks through adding text data, integrating OWL-based custom ontologies, and querying for insights.
* [Use the API](/tutorials/use-the-api) to programmatically manage your knowledge graphs, run queries, and integrate with other applications.
````

## File: content/use-cases.mdx
````
---
title: Use Cases
asIndexPage: true
---

export function generateMetadata() {
  return {
    title: "Cognee - Use Cases",
    description: "Use cognee for chatbots. Codegraph and code assistant with cognee.",
    alternates: {
      canonical: "https://www.docs.cognee.ai/use-cases",
    },

    openGraph: {
      url: "https://www.docs.cognee.ai/use-cases",
      type: "website",
      title: "Cognee - Use Cases",
      description: "Use cognee for chatbots. Codegraph and code assistant with cognee.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },

    twitter: {
      site: "@cognee_",
      card: "summary_large_image",
      title: "Cognee - Use Cases",
      description: "Use cognee for chatbots. Codegraph and code assistant with cognee.",
      images: ["https://www.cognee.ai/images/meta/cognee-logo-text-on-gradient.png"],
    },
  };
}


#  Intro

With the arrival of ChatGPT, asking human-like questions to complex data systems has become possible.
We can now **connect** our data to AI models.
But despite advancements and promising results, these systems often struggle to deal with the messy realities of our data:

1. **Complex Data and Scale:**
   Many companies have databases spanning hundreds of tables. LLMs have a difficulty to capture the scale or interconnected complexity found in real business environments.

2. **Real-World Relevance:**
   Common LLM answers  often ignore the operational questions that executives, analysts, and teams rely on. These might include performance metrics, key insights into user behavior, or specific compliance-related questions.

3. **Lack of Business Context:**
   Without rich metadata, domain ontologies, and transformations that bring real-world meaning to the data, even the most advanced LLMs can produce “hallucinations”—answers that are plausible-sounding but incorrect. This erodes trust and diminishes the value of AI-driven insights.


**Knowledge Graphs (KGs)** offer a promising solution. By layering on business context—such as linking data points to specific domains, categories, and hierarchies—KGs help LLMs produce more accurate and explainable outputs.
These systems can capture the complex domain rules in order to solve problems that LLMs are not trained on.

---

## Use Cases

### 1. Chatbots
**Scenario:**
A gaming company wants their support team to know details about their users from 1000s of chats:
- *"Amy broke her leg and had a really bad couple of weeks?"*
- *"John likes to go hiking and learn new languages. He speaks 4 fluently and frequently mentions his trips to Europe"*
- *" Rita spent 200 USD in the past week on bonuses and she struggles with the level 13"*

**Challenge:**
Their data spans thousands of interactions, multiple tables, and complex systems.

**Solution:**
Read about our implementation [here](use-cases/chatbots.md)

### 2. Code analysis for coding assistants
**Scenario:**
A developer using coding assistants needs an answers that needs to include a dozen of files and understand how different parts of the system relate to each other:
- *"If I change X variable, and improve Y function, where in the system do I need to change other settings for code to work"*
- *"How can I update Z function with new parameters and how would the API need to be changes?"*

**Challenge:**
Complex codebases have many links between the files, and typical SOA systems only allow for interacting with a few files disconnected files that can fit LLM context window
**Solution:**
Read about our implementation [here](use-cases/code-assistants.md)

### 3. HR
**Scenario:**
A company providing HR services needs to answer questions like:
- *"List all the candidates that have more than 5 years of experience"*
- *"What are the people who got promoted at their work in the first 6 months"*

**Challenge:**
Reasoning over a large number of PDFs and answering complex questions is not well implemented with RAG solutions and usually breaks down them more data you add
**Solution:**
Read about our implementation [here](use-cases/human-resources.md)

---

### Why This Matters

- **Better, Faster, Stronger:**
  With enhanced accuracy and context, AI Agents and Apps can answer questions accurately in production

- **Reduced Errors and “Hallucinations”:**
  By connecting LLMs to KGs, the system’s output is rooted in real data, not guesswork.

- **Improved Trust and Adoption:**
  Explainable results, help to use LLMs as part of everyday operations.
````
