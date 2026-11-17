### 1. AI Testing Prompt

> "I am working on an LLM that is a campus resource for a university. I have the code and the program works, however, I now need to write tests from pseudocode. These are the directions:
> Create a file called `test_agent.py` in your `campus_agent` folder. It should contain tests that verify:
>
> - **TEST 1: `test_library_lookup`**
>
>   - WHEN we call `get_campus_resource_info("library")`
>   - THEN it should return a dictionary with status `"success"`
>   - AND the returned resource should have name `"Library"`
>
> - **TEST 2: `test_tutoring_alias`**
>
>   - WHEN we call `get_campus_resource_info("tutoring")`
>   - THEN it should return a dictionary with status `"success"`
>   - AND the returned resource should have name `"Tutoring Center"` _(This verifies that aliases work)_
>
> - **TEST 3: `test_case_insensitive`**
>
>   - WHEN we call `get_campus_resource_info("LIBRARY")`
>   - THEN it should return a dictionary with status `"success"`
>   - AND the returned resource should have name `"Library"` _(This verifies case-insensitivity)_
>
> - **TEST 4: `test_resource_not_found`**
>
>   - WHEN we call `get_campus_resource_info("dental office")`
>   - THEN it should return a dictionary with status `"error"`
>   - AND the returned dictionary should have an `error_message`
>   - AND the `error_message` should contain the phrase `"Available resources"`
>
> - **TEST 5: `test_list_all_resources`**
>   - WHEN we call `get_campus_resource_info("all")`
>   - THEN it should return a dictionary with status `"success"`
>   - AND it should have an `available_resources` key
>   - AND `available_resources` should be a list with at least 4 items"

---

### 2. The Test Code You Ended Up With (or a Summary)

The test code I ended up using can be found in the `test_agent.py` file. There’s a function each for testing library lookup, verification that aliases work correctly, testing for case insensitivity, testing if a resource does not exist or is not found, and finally listing all available resources. I chose to designate a function for each test to make for better readability and make future updates easier to implement.

---

### 3. What You Verified: Did the Tests Pass? What Did You Check?

My tests all passed with the exception of Test #2 where I had to test the tutoring alias. I initially thought that there was something wrong with the AI-generated code, but I soon realized that it was failing because I didn't have the Tutoring Center as one of my campus resources.

I also asked the agent if the generated testing code was too verbose and if it could be optimized. It did provide a shortened code that was not too repetitive, but I thought it made it more difficult to read and harder for future developers to add to it. Additionally, it wasn't expressly clear what it was testing since it combined functions to be more efficient, so I made the decision to keep the longer code because I felt more comfortable with it and thought that it'd be easier to update in the future.

---

### 4. What You Changed and Why: Did You Modify the AI's Output? Why?

My `campus_resources.json` file did not have a tutoring listing, so I decided to add it to the file. I thought it would be faster and easier for me to change the JSON file than to change the Python test with another alias. I kept the rest of the tests the same, and after quickly updating my JSON file, all tests passed at 100%.

---

### 5. Your CI/CD Workflow Prompt (if you used AI) or "I wrote the YAML manually"

My CI/CD workflow was a little more tenuous, so I spent the majority of my time trying to figure out what was happening. The agent I used wrote my YAML file, but I kept hitting roadblocks. The agent recommended changing the location of my `test_agent.py` file to the root directory instead of keeping it in the `campus_agent` directory, as our lab directed. I ran into paths that were not being found, imports that were erroneous, and bad recommendations on changing file structures. All of this was obviously causing my GitHub Actions to fail. I looked up what the errors I was receiving meant and worked backwards from there. Eventually, I manually updated file paths and pasted some of the errors into the agent, and I was able to get a successful run in my Actions tab in GitHub.

---

### 6. The Workflow You Ended Up With (or a Summary)

My YAML file sets up an automated testing and deployment pipeline for the Campus Agent. Whenever code is pushed to `main`, GitHub Actions creates an Ubuntu environment with Python 3.11, installs all dependencies, and runs `pytest` on the test suite. Those tests ensure that the agent handles case-insensitivity, correct resource retrieval, error messaging, and full listing queries reliably every single time.

---

### 7. What You Changed and Why: Same as Above

The YAML file that was generated kept giving me errors, so after looking up errors and doing a bit of preference tuning, I was able to get a good base and just updated file paths as needed. Everything else pretty much stayed the same.

---

### Final Reflection

The code that the AI agent wrote was better than what I could write. My knowledge in Python is basic and admittedly rusty. Some of the necessary bits of code, like assertions, I had never even used, so having a better code writer was definitely more helpful. However, I also recognized how much frustration and extra time it added to my work, so it's not infallible by any means.

I recognized the generated code was also verbose and repetitive, so I can absolutely see it veering into "SlopCodeBench". I personally decided to keep the more verbose code because I could understand it better, it seemed more organized, and potentially would be easier for future developers to work on. That being said, I'm sure that the code could have been optimized more, especially for a more experienced programmer.

Next time I write a prompt for AI, I can be more specific from the start, defining what the non-negotiables are and including relevant context. Although my process fine-tuned the response, I could have saved more time by being more deliberate and purposeful in the beginning.

Students have a wide variety of circumstances, ranging from run-of-the-mill basic questions like hours for a particular office to something more urgent like medical or food needs. Although our Campus Agent is a prototype, it makes the effort that much more worth it if it can be used by fellow and potentially future students.
