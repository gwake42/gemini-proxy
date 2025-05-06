# MapsIndoors SDK Knowledge Base

This structured knowledge base is designed for use with AI models like Claude or Gemini.
It organizes the core functions, customization points, and implementation flows of the MapsIndoors SDK in a way that enables intelligent querying, embedding, and augmentation.

## Structure

The `mapsindoors_knowledge_base.json` file is organized into:

- **sections[]**: A list of named SDK feature areas
  - `id`: Section number
  - `title`: Title or heading of the SDK section
  - `summary`: A short description of what the section covers
  - `code`: The relevant implementation or code snippet

## Example Entry

```json
{
  "id": 1,
  "title": "getConferenceRooms",
  "summary": "Filters and retrieves conference rooms using MapsIndoors LocationService.",
  "code": "async function getConferenceRooms(options = {}) { ... }"
}
```

## Suggested Usage

- **AI Prompt Injection**: Feed sections directly into context windows for question answering or code generation.
- **Searchable UI**: Build an app that filters `sections[]` based on keywords or features.
- **Custom Extensions**: Add new sections with your own integrations or vertical-specific examples.

## File Location

- [`mapsindoors_knowledge_base.json`](./mapsindoors_knowledge_base.json)

