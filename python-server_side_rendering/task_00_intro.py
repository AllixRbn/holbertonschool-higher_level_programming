import os


def generate_invitations(template, attendees):
    # Checks template type
    if not isinstance(template, str):
        print(f"Error: invalid input type for template "
              f"({type(template).__name__})")
        return None

    # Checks attendees type
    if not isinstance(attendees, list):
        print(f"Error: invalid input type for attendees "
              f"({type(attendees).__name__})")
        return None

    # Checks that all attendees are dictionaries
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: attendees must be a list of dictionaries.")
            return None

    # Checks empty template
    if template == "":
        print("Template is empty, no output files generated.")
        return None

    # Checks empty attendees list
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return None

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        output = template

        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            output = output.replace("{" + key + "}", str(value))

        filename = f"output_{index}.txt"

        try:
            if os.path.exists(filename):
                os.remove(filename)

            with open(filename, "w", encoding="utf-8") as file:
                file.write(output)

        except Exception as e:
            print(f"Error writing file {filename}: {e}")
