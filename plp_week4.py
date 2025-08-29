import os

def modify_content(content):
    """Modify the file content - in this case, convert to uppercase"""
    return content.upper()

def main():
    print("📁 File Read & Write Challenge 🖋️")
    print("=" * 40)
    
    # Get filename from user
    filename = input("Please enter the filename to read: ").strip()
    
    try:
        # Check if file exists
        if not os.path.exists(filename):
            raise FileNotFoundError(f"The file '{filename}' does not exist.")
        
        # Check if we have read permission
        if not os.access(filename, os.R_OK):
            raise PermissionError(f"You don't have permission to read '{filename}'.")
        
        # Read the file
        with open(filename, 'r') as file:
            content = file.read()
        
        print(f"✅ Successfully read '{filename}'")
        
        # Modify the content
        modified_content = modify_content(content)
        
        # Create output filename
        name, ext = os.path.splitext(filename)
        output_filename = f"{name}_modified{ext}"
        
        # Write to new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"✅ Successfully created modified file: '{output_filename}'")
        print(f"📊 Original size: {len(content)} characters")
        print(f"📊 Modified size: {len(modified_content)} characters")
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
    except PermissionError as e:
        print(f"❌ Error: {e}")
    except IOError as e:
        print(f"❌ I/O Error: {e}")
    except UnicodeDecodeError:
        print(f"❌ Error: Cannot decode the file. It might be a binary file.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    finally:
        print("\n" + "=" * 40)
        print("Thank you for using the File Modifier!")

if __name__ == "__main__":
    main()