#! /usr/bin/env python

import argparse

from flask import Flask, render_template
from flask_graphql import GraphQLView

from graphql_api.schema import schema

app = Flask(__name__,
            static_folder="../client/dist", static_url_path="",
            template_folder="../client/dist")


@app.route("/")
def index():
    return render_template("index.html")


app.add_url_rule('/api/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple Flask-GraphQL Server')
    parser.add_argument('-d', '--debug', action="store_true", default=False)
    parser.add_argument('-v', '--verbose', action="store_true", default=False)
    args = parser.parse_args()

    app.run()
