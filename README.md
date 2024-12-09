# INT-PROJECT: Text to Interactive Graph Generator  

### How to Contribute:  

Primary Components:  
1. Backend Components  
	1.1 NLP Pipeline  
	- Text Preprocessing: Clean and tokenize input text.  
	- Named Entity Recognition (NER): Extract entities (e.g., names, organizations, locations).  
		- Tools: spaCy, Hugging Face Transformers.  
	- Relation Extraction: Identify relationships between entities (e.g., "works for", "met with").  
		-Tools: Rule-based approach or fine-tuned Transformer models.  
	1.2 Graph Database Integration  
	- Database Schema Design: Define node types (e.g., Person, Organization) and relationships (e.g., "works with", "associated with").  
	- Neo4j Integration: Use Python’s py2neo or neo4j package for CRUD operations on graph data.  
	1.3 RESTful API  
	- FastAPI Endpoints:  
		- POST /process_text: Accept raw text, extract entities/relationships, and store in the database.  
		- GET /fetch_graph: Fetch graph data for rendering.  
		- POST /expand_node: Expand a specific node dynamically by querying relationships.  
	1.4 Knowledge Memory  
	- Caching: Use Redis for fast access to frequently queried nodes.  
	- Persistence: Ensure knowledge is permanently stored in Neo4j.  

2. Frontend Components  
	2.1 User Interface  
	- Text Input Component: Allow users to enter raw text or upload files.  
	- Graph Viewer: Display the knowledge graph interactively.  
	- Libraries: Cytoscape.js or vis.js.  
	2.2 Graph Interaction  
	- Dynamic Node Expansion: On-click, fetch related nodes and update the graph in real time.  
	- Search Bar: Enable users to search for specific entities in the graph.  
	2.3 Visualization Features  
	- Filter Options:  
		- Filter nodes by type (e.g., Person, Organization).  
		- Filter relationships by type (e.g., "associated with", "works with").  
	- Customizable Layouts: Support for different graph layouts (e.g., hierarchical, radial).  

3. Core Logic  
	3.1 Entity Matching and Deduplication  
		- Node Consolidation: Avoid duplicate nodes by matching attributes (e.g., name, nationality).  
		- Fuzzy Matching: Handle minor differences in text (e.g., "Dave" vs. "David").  
	3.2 Relationship Management  
		- Weighted Relationships: Assign weights to edges based on the strength or type of connection.  
		- Temporal Information: Include timestamps if applicable.  
	3.3 Error Handling  
		- Validation: Check for incomplete or inconsistent data.  
		- Fallbacks: Default behaviors when entity/relationship extraction fails.  

4. Deployment and Scalability  
	4.1 Backend Deployment  
		- Local Setup: Dockerize FastAPI and Neo4j for easy local deployment.  
		- Cloud Deployment: Host on AWS/GCP/Azure.  
	4.2 Frontend Deployment  
		- Use Vercel or Netlify for frontend hosting.  
	4.3 CI/CD Pipeline  
		- Automate testing and deployment using GitHub Actions.  

5. Enhancements (Future Features)  
	5.1 Bulk Data Ingestion  
		- Process large datasets (e.g., CSV or JSON files) and integrate into the graph.  
	5.2 Natural Language Query Interface  
		- Allow users to ask questions in plain English (e.g., "Who is associated with GreenWell Foundation?").  
	5.3 Advanced Visualizations  
		- Heatmaps, clustering, or centrality metrics for graph insights.  
	5.4 Export Options  
		- Export graphs as JSON, CSV, or images.  
	5.5 Collaborative Features  
		- User accounts for saving and sharing graphs.  
	5.6 ChatGPT Integration for Summarized Reports  
	5.7 Make the Product Suitable for all Forms, Scales, Types of Data Analysis & Visualizations  

  
Directory Structure - Please Update the Directory as the Project Advances. 
```
knowledge_graph_project/
├── main.py
├── requirements.txt
├── src/
    ├── nlp_pipeline.py
    ├── entity_extraction/
        ├── ner_model.py
        ├── relation_extraction.py
    ├── utils/
        ├── text_cleaner.py
├── tests/
    ├── test_nlp_pipeline.py
```
