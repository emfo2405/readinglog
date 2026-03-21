## Readinglog - API
Jag har skapat ett API för att kunna hantera lässtatusar samt bokrecensioner. API:et är skapat i syfte att kunna använda Create, Read, Update, Delete genom GET, POST, PUT, PATCH och DELETE. API:et är skapat med Django och använder även den inbyggda user-funktionaliteten.

### Anslutning till API
API:et är publicerat på Render och har URL:en: https://readinglog-65ok.onrender.com.   

### Tabeller i databasen
De tabeller som är skapade som modeller i backendtjänsten är en för bokrecension, en för lässtatus och en för bok. Tanken med API:et är att kunna koppla till Google Books API och därmed finns google_books_id som parameter för tabellerna lässtatus och recension. Men även en tabell för böcker finns ifall böcker skulle behöva sparas i databasen.

#### Tabell för recension
| Tabellnamn  | _id | user | google_book_id | content | review | created_at |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | 
| Review  | SERIAL PRIMARY KEY  | INTEGER NOT NULL FOREIGN KEY  | STRING  | STRING | INTEGER NOT NULL | DATE AUTO ADDED | 

#### Tabell för lässtatus
| Tabellnamn  | _id | user | google_book_id | status | pages_read | started_at | finished_at |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | 
| ReadingStatus  | SERIAL PRIMARY KEY  | INTEGER NOT NULL FOREIGN KEY  | STRING  | STRING ("TOREAD", "READING", "READ") | INTEGER | DATE | DATE |

#### Tabell för bok
| Tabellnamn  | _id | google_id | title | author | description | image | pages |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Book  | SERIAL PRIMARY KEY  | STRING UNIQUE  | STRING  | STRING | STRING | STRING | INTEGER | 



### Hur man använder API:et 
Det finns olika sätt att använda API:et för att nå det, nedan finns en tabell över vilka metoder som kan användas och vad de innebär. 

| Metod  | Ändpunkt | Beskrivning | 
| ------------- | ------------- | ------------- |
| GET | /api | Kopplar upp till API |
| GET | /api/review/ | Hämtar in alla publicerade recensioner i databasen |
| GET | /api/review/{id}/ | Hämtar in en recension med givet id |
| POST | /api/review/ | Skapar en ny recension om korrekt information skickas med. Token behöver skickas med. |
| PATCH | /api/review/{id}/ | Uppdaterar information om en recension med givet id med korrekt medskickad information. Token behöver skickas med. |
| DELETE | /api/review/{id}/ | Raderar en recension med givet id. Token behöver skickas med. |
| GET | /api/readingstatus/ | Hämtar in alla publicerade lässtatusar i databasen |
| GET | /api/readingstatus/{id}/ | Hämtar in en lässtatus med givet id |
| POST | /api/readingstatus/ | Skapar en ny lässtatus om korrekt information skickas med. Token behöver skickas med. |
| PATCH | /api/readingstatus/{id}/ | Uppdaterar information om en lässtatus med givet id med korrekt medskickad information. Token behöver skickas med. |
| DELETE | /api/readingstatus/{id}/ | Raderar en lässtatus med givet id. Token behöver skickas med. |
| GET | /api/book/ | Hämtar in alla publicerade böcker i databasen |
| GET | /api/book/{id}/ | Hämtar in en bok med givet id |
| POST | /api/book/ | Skapar en ny bok om korrekt information skickas med. |
| PATCH | /api/book/{id}/ | Uppdaterar information om en bok med givet id med korrekt medskickad information. |
| DELETE | /api/book/{id}/ | Raderar en bok med givet id. |
| GET | /api/users/ | Raderar en bok med givet id. |
| POST | /api/login/ | Raderar en bok med givet id. |
| GET | /api/refresh/ | Raderar en bok med givet id. |
| POST | /api/register/ | Raderar en bok med givet id. |
| GET | /api/profile/ | Raderar en bok med givet id. |



#### Ett objekt som lägger till korrekt information om en recension är uppbyggt så här:
```
{
  "user": user-id,
  "google_books_id": book-id,
  "content": "Valfritt innehåll",
  "review": 10
}
```

#### Ett objekt som lägger till korrekt information om en lässtatus är uppbyggt så här:
```
{
  "user": user-id,
  "google_books_id": book-id,
  "status": "READ",
  "pages_read": 100,
  "startes_at": 2026-03-10,
  "finished_at": 2026-03-21
}
```

#### Ett objekt som lägger till korrekt information om en bok är uppbyggt så här:
```
{
  "google_id": book-id,
  "title": "Bokens titel",
  "author": "Författarens namn",
  "description": "En beskrivning"
  "image": "bild-url"
  "pages": 250
}
```

#### Ett objekt som lägger till korrekt information om en användare för registrering är uppbyggt så här:
```
{
  "username": "Användarnamn",
  "email": "E-post",
  "password": "Lösenord"
  "password2": "Upprepa lösenord"
}
```

#### Ett objekt som lägger till korrekt information om en användare för inloggning är uppbyggt så här:
```
{
  "username": "Användarnamn",
  "password": "Lösenord"
}
```
