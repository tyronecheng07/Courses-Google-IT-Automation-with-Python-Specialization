#example regular expression
import re
def check_zip_code(text):
  result = re.search(r" [0-9]{5}", text)
  return result != None
  

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False

#example 2
import re
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z\s]*[.?!]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True

#[A-Z] first letter
#[a-z\s]* the rest
#[.?!] last letter

#example 3
import re
def check_time(text):
  pattern = r"^[0-2]?[0-9]:[0-5][0-9]\s?[APap][Mm]$"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False

#example 4
import re
def check_web_address(text):
  pattern = r"[\w\.\+-]*\.[a-zA-Z]*[a-zA-Z]$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

#example 5
import re
def contains_acronym(text):
  pattern = r"[A-Z]?[a-z\s]*\([A-Za-z0-9]*[A-Za-z0-9]\)[a-z\s!]*" 
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

#example 6
import re
def rearrange_name(name):
  result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)

#advance example 1
import re
def long_words(text):
  pattern = r"\w{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []

#advance example 2
import re
def extract_pid(log_line):
    regex = r"\[(\d+)\]: ([A-Z]{5,7})"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)

#advance example 3
import re
def transform_record(record):
  pattern = r"\b(\d{3}-\d{3}-?\d{4})\b"
  string = "+1-"
  new_record = re.sub(pattern, string+r"\1" , record)
  
  return new_record
####### -? means that - can be ignored in some case
print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer

#advance example 4
import re
def multi_vowel_words(text):
  pattern = r"\b(\w*[aeiou]{3,}\w*)\b"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []

#advance example 5
import re
def transform_comments(line_of_code):
  result = re.sub(r"[#]{1,3}", "//", line_of_code)
  return result


print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"
