from google.adk.tools.tool_context import ToolContext


def add_fact_to_notes(fact_text: str, tool_context: ToolContext):
    """
    Appends a verified fact to a text file.
    Args:
        fact_text: The text content to save.
    """
    try:
        with open("notes.txt", "a", encoding="utf-8") as file:
            file.write(f"- {fact_text}\n")

        return "SUCCESS: Fact has been successfully added to notes.txt."

    except IOError as e:
        return f"ERROR: Could not write to file. System reported: {e}"
    except Exception as e:
        return f"ERROR: An unexpected error occurred: {e}"
