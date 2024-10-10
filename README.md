## Endpoints

### 1. Get all todos
**GET** `/todos`

Retrieves a list of all todo items.

**Response:**
```json
[
  {
    "id": 1,
    "title": "Sample Todo",
    "completed": false
  }
]
```

### 2. Create a new todo
**POST** `/todos`

Creates a new todo item.

**Request Body (JSON):**
```json
{
  "title": "New Todo",
  "completed": false
}
```
**Response:**
```json
{
  "id": 2,
  "title": "New Todo",
  "completed": false
}

```

### 3. Update an existing todo
**PUT** `/todos:id`

Updates a todo item by its ID.

**Request Body (JSON):**
```json
{
  "title": "Updated Todo",
  "completed": true
}
```
**Response:**
```json
{
  "id": 2,
  "title": "Updated Todo",
  "completed": true
}
```

### Delete a todo
**DELETE** `/todos:id`

Deletes a todo item by its ID.

**Response:**
Status `204 No Content` on success.
```json
{
}
```
https://elements.getpostman.com/redirect?entityId=38237977-addc38fc-91d1-4b76-ae98-de5d6b334b61&entityType=collection
