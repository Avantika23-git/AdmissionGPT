from brain import chat

while True:

    message = input("\nYou : ")

    result = chat(message)

    print("\nAdmissionGPT :")

    if result["type"] == "prediction":

        print("\nTop Branch Predictions:\n")
        print(result["branches"])

        print("\nCutoff Analysis:\n")
        print(result["cutoffs"])

    else:

        print(result["answer"])