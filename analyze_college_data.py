from utils import load_json_to_dict, save_dict_to_json
import os

current_date = "2025-12-29"

cwd = os.getcwd()
fpname = f"{cwd}/data/all_colleges_{current_date}.json"

SCHOOLS = f"{cwd}/data/schools.json"

def analyze_data_1(filename):
  print(filename)
  data = load_json_to_dict(filename)
  schools = {}
  for item in data:
    latest = item.get("latest", {})
    if not latest:
      break
    school = latest.get("school", {})
    if not school:
      break
    sname = school.get("name", "")
    if not sname:
      break
    temp = {
      "name": sname
    }
    szip = school.get("zip", "")
    scity = school.get("city", "")
    sstate = school.get("state", "")
    saddress = school.get("address", "")
    saccreditor = school.get("accreditor", "")
    sschool_url = school.get("school_url", "")
    speps_ownership = school.get("peps_ownership", "")
    saccreditor_code = school.get("accreditor_code", "")
    sfaculty_salary = school.get("faculty_salary", "")
    temp["zip"] = szip
    temp["city"] = scity
    temp["state"] = sstate
    temp["address"] = saddress
    temp["accreditor"] = saccreditor
    temp["school_url"] = sschool_url
    temp["peps_ownership"] = speps_ownership
    temp["accreditor_code"] = saccreditor_code
    temp["faculty_salary"] = sfaculty_salary
    
    student = latest.get("student", {})
    if student:
      ssize = student.get("size", "")
      sgrad_students = student.get("grad_students", "")
      temp["student_count"] = ssize
      temp["grad_student_count"] = sgrad_students
      
    admissions = latest.get("admissions", {})
    sat_scores = admissions.get("sat_scores", {})
    s75th_percentile = sat_scores.get("75th_percentile", {})
    if s75th_percentile:
      sat_math = s75th_percentile.get("math", "")
      sat_writing = s75th_percentile.get("writing", "")
      sat_critical_reading = s75th_percentile.get("critical_reading", "")
      temp["sat_math"] = sat_math
      temp["sat_writing"] = sat_writing
      temp["sat_critical_reading"] = sat_critical_reading
      
    programs = latest.get("programs", {})
    cip_4_digits = programs.get("cip_4_digit", [])
    if cip_4_digits:
      sprograms = {}
      for cip_4_digit in cip_4_digits:
        name = cip_4_digit.get("title", "")
        credential = cip_4_digit.get("credential", {})
        degree_title = credential.get("title", "")
        cip_school = cip_4_digit.get("school", {})
        school_name = cip_school.get("name", "")
        school_type = cip_school.get("type", "")
        sprograms[name] = {
          "name": name,
          "degree_title": degree_title,
          "school_name": school_name,
          "school_type": school_type
        }
      temp["school_programs"] = sprograms
    schools[sname] = temp
  save_dict_to_json(schools, SCHOOLS)

# run
analyze_data_1(fpname)
