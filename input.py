import chardet


class Input:
    question = "Find all kinds of errors, including logical ones, and provide hints for their correction or improvement, including suggestions for code style."
    instruction1 = "ExampleInstruction" #replace with actual instruction
    instruction2 = "ExampleInstruction2" #replace with actual instruction

    @staticmethod
    def generate_prompt(submission_id: str) -> str:
        student_submission = Input.javacode_as_string(submission_id)
        if int(submission_id) < 80000: #replace with suitable number or condition
            prompt = f"{Input.instruction1}\n{Input.question}\n{student_submission}"
        else:
            prompt = f"{Input.instruction2}\n{Input.question}\n{student_submission}"
        return prompt

    @staticmethod
    def javacode_as_string(submission_id: str):

        # Define the path to your Java file
        if int(submission_id) < 80000:
            java_file_path = "submissions/" + submission_id + ".java"  #replace with actual filepath
        else:
            java_file_path = "filepath" #replace with actual filepath
        try:
            with open(java_file_path, "r", encoding='utf-8') as file:
                java_code = file.read()
        except UnicodeDecodeError:
            with open(java_file_path, 'rb') as file:
                result = chardet.detect(file.read())
                encoding = result['encoding']
                with open(java_file_path, 'r', encoding=encoding) as f:
                    java_code = f.read()
        return java_code