def hello(name,lang):
    greetings={
        "English": "Hello",
        "spanish" : "Hola",
        "German" : "Hallo",
    }
    msg = f"{greetings[lang]} {name}"
    print(msg)

if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="provide a personal greeting"
    )
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True,
        help="name of the person to greet"
    )
    parser.add_argument(
        "-l","--language",metavar="language",
        required=True,choices=["English","Spanish","German"],
        help="The Language of the greetings."
    )
    args = parser.parse_args()
    hello(args.name,args.language)

# args => object of parser.parse_args(analyse the input of the user)Argument Name Mismatch: The argument added for the language is --language, but you’re trying to access it with args.lang in the function call. It should be args.language.
# args go through data through your options -n , -l
# what is metavar(appear in help message) required, its restrictions(options)
