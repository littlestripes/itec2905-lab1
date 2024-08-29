if __name__ == "__main__":
    num_classes = int(input("How many classes are you taking this semester? "))

    class_names = []
    for _ in range(0, num_classes):
        class_names.append(str(input("Enter the name of the class: ")))

    print("This semester, you're taking:")
    for class_name in class_names:
        print(class_name)
