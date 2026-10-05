**The Problem**

Jamestown Community College offers many different resources to students, such as the library,
tutoring center, advising office, the food pantry and more. However, many students are not
aware of these resources or are unsure of where or how to find them. This project aims to
solve that problem by making these resources available and easily found for students so that
they can get the services they need.

**Gemini's Limitations**

A large language model (LLM) like Gemini is trained on public information. However, it does
not have information that is private, local, or frequently changing like the information
that may be found in a campus directory. Knowing these limitations and still trying to coax
an answer out of Gemini can result in no answer being returned, an attempt to look it up
online (where more stale information may be), or a hallucination.

**Why a separate JSON file is used**

1. A JSON file separates data from logic so a future developer can update these office hours
   without needing to read or edit Python.
2. It makes the information independantly reviewable so an instructor, another student, or
   even Student Services can verify the data without having to necessarily understand the code.
3. It prepares the project for later growth since it's easy to replace a JSON file with a
   database, API, or content management system and the agent wouldn't need to change.

**Limitation & Improvements**

1. _Limitation:_ The data can become stale.
   _Improvement:_ Add last_verified dates; verify info against the college website, or pull from
   a live feed.

2. _Limitation:_ The system is only as trustworthy as its source data.
   _Improvement:_ Put a human verification check in every resource; output "Error" instead
   of inventing data.

3. _Limitation:_ Rate limits may pause heavy use.
   _Improvement:_ Future versions can queue or cache frequently asked questions.

**What's so bad about wrong info?**

If campus information in the JSON file is inaccurate, it renders the agent useless and can
be harmful to students or those who need help. Students will not be able to look up resources and
if they are, they will be given wrong information which will not allow them to access the
resources they need.

Implementing verified_by and last_verified fields will allow us to audit and update the
system over time and hopefully prevent the agent from dispensing inaccurate information.

**Campus Information**
| Resource | Location | Hours | Phone | Email | Website | Verified By | Date Verified |
|---|---|---|---|---|---|---|---|
| Library | 525 Falconer Street, Jamestown; 260 North Union Street, Olean | Jamestown: Monday-Thursday: 8 a.m. - 6 p.m. & Friday: 8 a.m. - 4 p.m.; Cattaraugus: Monday-Thursday: 8 a.m.-4 p.m., Friday: 8 a.m.-1 p.m. | 716.338.1008 - Jamestown; 716.376.7517 - Olean | None Listed | [Link](https://www.sunyjcc.edu/support/learning-commons/library/ask) | Jerrica Sosa | 2026-10-02 |
| Academic Advising | None listed | By appointment | 716.338.1065 | SuccessCenter@sunyjcc.edu | [Link](https://www.sunyjcc.edu/support/success-center/advising/get-connected) | Sameer Patel | 2026-09-29 |
| Student Food Pantry | Jamestown Campus: next to the Campus Bookstore, Hamilton Collegiate Center, first floor; Cattaraugus County Campus: Success Center across from the bookstore, College Center, first floor | None listed | Jamestown Campus: 716.338.1004; Cattaraugus County Campus: 716.376.7508 | None listed | [Link](https://www.sunyjcc.edu/support/get-help/food-pantry) | Jerrica Sosa | 2026-09-22 |
| Health Center | Jamestown Campus: COCE 122; Cattaraugus County Campus: COLL 139 | None listed | 716.338.1013 (Charlene Johnson, General); 716.338.1014 (Shelly Wells, RN, Nurse) | HealthCenter@sunyjcc.edu | [Link](https://www.sunyjcc.edu/support/health-center) | Jerrica Sosa | 2026-09-22 |
| Financial Aid Office | COCE Floor 1, Jamestown Campus | Contact office for hours | 716.338.1009 | FinancialAid@sunyjcc.edu | [Link](https://www.sunyjcc.edu/support/financial-aid-billing) | Tangie Cummings | 2026-09-29 |
| IT Help Desk | Floor 1 of the Hultquist (HULT) building | Monday through Friday, 8:30 AM – 4:30 PM | 716.338.1122 | JCCHelpDesk@mail.sunyjcc.edu | [Link](https://jcc.helpdesk.sunyjcc.edu/servicedesk/customer/user/login?destination=portals) | Shant Michaelian | 2026-09-26 |
| Campus Bookstore | JCC Campus Store. 525 Falconer Street. Jamestown. NY 14701 | Mon-Thu: 9:00 AM - 4:30 PM. Fri: 9:00 AM - 2:00 PM. Sat-Sun: Closed | (877) 420-1734 | sm8369@bncollege.com | [Link](https://sunyjcc.bncollege.com/) | Maryam Fatima | 2026-09-30 |
| Campus Safety | Jamestown Campus (Hamilton Collegiate Center) | Contact office or campus safety cell for active hours | 716.338.1015 | Not listed | [Link](https://cm.maxient.com/reportingform.php?SUNYJamestownCC&layout_id=5) | Maryam Fatima | 2026-09-30 |
| Career Services | Jamestown Campus and Cattaraugus County Campus (Olean) | Contact office for appointment hours | 716.338.1061 | Not listed | [Link](https://www.sunyjcc.edu/support/career-services/interest) | Maryam Fatima | 2026-09-30 |
