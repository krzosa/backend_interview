## Backend interview

A test project for a Backend Developer position.

Plenty of various data vaults/lakes/warehouses are around. Why not implement our own? Let's follow the WORM[3] principle and implement simple repository which stores any data user provides. Everytime user provides the data, a fingerprint for this data is being generated so we can uniquely identify this piece of data.


Requirements:

* Pick some HTTP server (but don't go for a framework way, ie. Django, it is not needed here) and consume `openapi.yaml` file;
* Implement two endpoints that are specified in `openapi.yaml` and provide simple input validation for these endpoints, according to the OAS[1];
* Store the schemas `payload` in the simplest datastore you can imagine;
* Generate a fingerprint (use some hash function for it, ie. SHA256) for the `payload` you've uploaded via `POST /schemas` and return this fingerprint as hashlink (see `openapi.yaml`);
* The same `payload` may be uploaded multiple times, but if it is already stored in the datastore, we do nothing (just return the fingerprint) as we implement idempotent operation[4];
* Provide README.md with essential info how to run it with some examples.

#### Examples

```
# 1.
POST /schemas
{ "payload": "bleble" }


response:
{ "hashlink": "708b1a7a6c6507b55ab537894493b61d46230ceeb21b605838a050a75c7ef0bb" }


# 2. Support for idempotent operation:
POST /schemas
{ "payload": "bleble" }


response:
{ "hashlink": "708b1a7a6c6507b55ab537894493b61d46230ceeb21b605838a050a75c7ef0bb" }


# 3.
GET /schemas/708b1a7a6c6507b55ab537894493b61d46230ceeb21b605838a050a75c7ef0bb

response:
{ "payload": "bleble" }
```

### Caveats

Since it's more a concept app, it’s perfectly fine to make some compromises:

* you can use whatever technology/framework is suitable for you (yet, please don't use a sledgehammer to crack a nut), the only interesing part is the enduser is able to run it and see the result;
      
      
Don't be neither too generic nor too specific – don't polish it too much, but also keep focus on the code as well  – your final product should be „just enough”.
* if you don't feel prepared for the job, either get familiar with languages/technologies you'd consider useful here, or let us know you're not ready for it;
* we'll notice if you've worked on it a week instead of a few hours – don't do more than it's specified in the requirements;


Your work should be available via GitHub as a public repository, commit often[2]. 

Value quality over quantity. And, finally, when in doubt – especially about the scope of the task – feel free to ask.



\[1\]: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.3.md

\[2\]: Get familiar with SRP principle (if you don't know it yet) and apply it to commits. Get familiar with this https://chris.beams.io/posts/git-commit/ . 

\[3\]: https://en.wikipedia.org/wiki/Write_once_read_many

\[4\]: https://stackoverflow.com/questions/1077412/what-is-an-idempotent-operation
