# ------------------------------------------------------------------------------------------------- #
# Title: Main Script
# # Description: Main script used for running application for module 8
# ChangeLog: (Who, When, What)
# Tellrell White, 06.13.2025, Created Script
# ------------------------------------------------------------------------------------------------- #

try:
    if __name__ == "__main__":
        import processing_classes as proc
        import presentation_classes as pres
        import data_classes as data
    else:
        raise Exception("This file starts the application and should not be imported.")
except Exception as e:
    print(e.__str__())

# Add error handling in main for reading and writing from file; add in employee objects to reduce dependency
#Add in comments at beginning of file to run main script and not other script and reduce imports

#---------------------- Beginning of the main body of this script------------------------------------#

#Reading data in from JSON file and storing it to a list
try:
    data.employees = proc.FileProcessor.read_employee_data_from_file(file_name=data.FILE_NAME,
                                                                     employee_data=data.employees,
                                                                     employee_type=data.Employee)  # Note this is the class name (ignore the warning)
except FileNotFoundError  as e:
    pres.IO.output_error_messages(e)

except Exception as e:
    pres.IO.output_error_messages(e)



# Repeat the follow tasks
while True:
    pres.IO.output_menu(menu=data.MENU)

    menu_choice = pres.IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            pres.IO.output_employee_data(employee_data=data.employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = pres.IO.input_employee_data(employee_data=data.employees, employee_type=data.Employee)  # Note this is the class name (ignore the warning)
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            proc.FileProcessor.write_employee_data_to_file(file_name=data.FILE_NAME, employee_data=data.employees)
            print(f"Data was saved to the {data.FILE_NAME} file.")
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
