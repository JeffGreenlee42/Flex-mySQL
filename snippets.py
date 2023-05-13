{
	"flask": {
        "prefix": "flask",
        "body": [
            "from flask import Flask, request, render_template, redirect, session",
            "app = Flask(__name__)",
            "",
            "@app.route('/')",
            "def index():",
            "\treturn 'Hello World!'\n",
            "",
            "if __name__=='__main__':",
            "\tapp.run(debug=True)",
        ],
        "description": "Flask Boilerplate"
    },

    "SQL": {
        "prefix": "SQL",
        "body": [
        "import pymysql.cursors",
        "class MySQLConnection:",
        "    def __init__(self, db):",
        "        connection = pymysql.connect(host = 'localhost',",
        "                                user = 'root',",
        "                                password = 'rootroot',",
        "                                db = db,",
        "                                charset = 'utf8mb4',",
        "                                cursorclass = pymysql.cursors.DictCursor,",
        "                                autocommit = True)",
        "        self.connection = connection",
        "    def query_db(self, query, data=None):",
        "        with self.connection.cursor() as cursor:",
        "            try:",
        "                query = cursor.mogrify(query, data)",
        "                print(\"Running Query:\", query)",
        "                cursor.execute(query, data)",
        "                if query.lower().find(\"insert\") >= 0:",
        "                    # INSERT queries will return the ID NUMBER of the row inserted",
        "                    self.connection.commit()",
        "                    return cursor.lastrowid",
        "                elif query.lower().find(\"select\") >= 0:",
        "                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES",
        "                    result = cursor.fetchall()",
        "                    return result",
        "                else:",
        "                    # UPDATE and DELETE queries will return nothing",
        "                    self.connection.commit()",
        "            except Exception as e:",
        "                # if the query fails the method will return FALSE",
        "                print(\"Something went wrong\", e)",
        "                return False",
        "            finally:",
        "                # close the connection",
        "                self.connection.close()",
        "def connectToMySQL(db):",
        "    return MySQLConnection(db)"
    ],
    "description": "MySQL Connection File"
    },

    "init": {
        "prefix": "init",
        "body": [
            "from flask import Flask",
            "",
            "app = Flask(__name__)",
            "",
            "app.secret_key = 'Py is life'",
        ],
        "description": "init py"
    },

    "server": {
        "prefix": "pyserver",
        "body" : [
            "from flask_app import app",
            "from flask_app.controllers import controllers_name",
            "if __name__=='__main__':",
            "\tapp.run(debug=True)"
        ]
    }
}