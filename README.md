# webapp-boilerplate

Boilerplate for a modern full-stack web application, customized to my liking.

[![Build Status](https://travis-ci.org/naim/webapp-boilerplate.svg?branch=master)](https://travis-ci.org/naim/webapp-boilerplate)

### Why do this?

"Webapp generators" generally come with a whole lot of bloat that is entirely unnecessary. Once upon a time it was a pain to wire up all these pieces, but that is essentially a non-issue at this point, so it's much more straightforward to do it all with yarn and webpack by hand.

### Project Structure

```
app
├── client
│   ├── package.json
│   ├── src
│   │   ├── App.jsx
│   │   ├── index.ejs
│   │   └── index.jsx
│   ├── webpack.config.js
│   └── yarn.lock
└── server
    ├── graphql_api
    │   ├── example
    │   │   ├── tests
    │   │   │   └── test_schema.py
    │   │   ├── mutations.py
    │   │   ├── queries.py
    │   │   └── types.py
    │   ├── mutation.py
    │   ├── query.py
    │   └── schema.py
    └── server.py
```

## Client

Babel + Flow, RxJS + React + Redux

## Server

Flask + Graphene
