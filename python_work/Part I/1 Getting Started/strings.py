
# 1.1.2 Changing Case in a String with Methods
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# 1.1.3 Using Variables in Strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

# 1.1.4 Using Variables in Strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

# 1.1.5 Adding Whitespace to Strings with Tabs or Newlines
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")

# 1.1.6 Stripping Whitespace
favorite_language = ' python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

nostarch_url = 'http://www.nostarch.com'
print(nostarch_url.strip('http://www.'))

# 1.1.7 Avoiding Syntax Errors with Strings
message = "One of Python's strengths is its diverse community."
print(message)

# 1.1.8 Exercise: Personal Message
first_name = "Eric"
message = f"Hello {first_name}, would you like to learn some Python today?"
print(message)

# 1.1.9 Exercise: Name Cases
name = "eric"
print(name.title())
print(name.upper())
print(name.lower())

# 1.1.10 Exercise: Famous Quote
famous_person = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new."
message = f"{famous_person} once said, \"{quote}\""
print(message)

# 1.1.11 Exercise: Stripping Names
name = " Eric "
print(name.strip())
print(name.rstrip())
print(name.lstrip())
print(name.strip())
