**The Problem**

Jamestown Community College offers many different resources to students, such as the library,
tutoring center, advising office, the food pantry and more. However, many students are not
aware of these resources or are unsure of where or how to find them. This project aims to
solve that problem by making these resources available and easily found for students so that
they can get the services they need.

**Gemini's Limitations**

A large language model (LLM) like Gemini is trained on public information. However, it does
not have information that is private, local or frequently changing like the information
that may be found in a campus directory. Knowing these limitations and still trying to coax
an answer out of Gemini can rsult in no answer being returned, an attempt to look it up
online (where more stale information may be) or a hallucination.

**Why a separate JSON file is used**

1. A JSON file separates data from logic so a future developer can update these office hours
   without reading or editing Python.
2. It makes the information independantly reviewable so an instructor, another student or
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

What could go wrong if the campus information in our JSON file is inaccurate?
Who should be responsible for verifying it?
If campus information in the JSON file is inaccurate, it renders the agent useless and can
be harmful to students or who need help. Students will not be able to look up resources and
if they are, they will be given wrong information which will not allow them to access the
resources they need.

Implementing verified_by and last_verified fields will allow us to audit and update the
system over time and hopefully prevent the agent from dispensing inaccurate information.

**Resource Location Hours Phone Email Website Verified By Date Verified**
Library
Tutoring Center
Advising
Financial Aid
