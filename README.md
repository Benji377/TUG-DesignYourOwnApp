# Design Your Own App - Winter Semester 2023/2024

[TeachCenter Course page](https://tc.tugraz.at/main/course/view.php?id=728)

## Course Overview

In this course, you will not only learn to design your own app but also utilize AI-assisted programming tools to enhance your coding experience. Here are some key aspects of the course:

- Use of Large Language Models (LLMs) like ChatGPT to assist in coding.
- Recommended AI tool: ChatGPT or alternatives like Bard, GitHub CoPilot, Perplexity AI, or locally self-hosted GPT4All.
- Each week, you will cover essential programming concepts and apply them to your project.
- The course consists of 7 individual Python practicals and your own application development project.
- Regularly document your work in the timetable below.
- Review interviews with teaching assistants to assess your understanding and progress.
- No final exam; your grade will be based on your performance throughout the course.

## Grading

Grading will be based on the following scale:

| Grade |                                                                   Requirements                                                                    |
|------:|:-------------------------------------------------------------------------------------------------------------------------------------------------:|
|     1 |   Excellent understanding, excellent code & tests, excellent project, excellent skill improvements & learning journey (> 90h) & applied for it.   |
|     2 |           Full & good understanding, good code & tests, good project, good skill improvement & obvious honest learning journey (> 75h).           |
|     3 |           Satisfying understanding of all concepts, OK code and tests, OK project, believable improvement and learning journey (> 75h).           |
|     4 | Obviously less effort than other students, e.g., no skill improvements, but understanding of all concepts there, and code + tests + project fine. |
|     5 |                                        None of the above (e.g., one of the concepts not fully understood).                                        |

**Note**: If you receive grade 5, you will have the opportunity for a "second chance" to improve your grade.


## Projects

You will implement 7 mini-projects and one larger project.
The programming language to use is Python (version 3.8 or newer).

| Project folder                       |          Concepts           | Suggested deadline |
|:-------------------------------------|:---------------------------:|:-------------------|
| [`01-datatypes`](01-datatypes)       |          Datatypes          | 2023-10-08         |
| [`02-variables`](02-variables)       |          Variables          | 2023-10-15         |
| [`03-functions`](03-functions)       |          Functions          | 2023-10-22         |
| [`04-tests`](04-tests)               |       Automatic tests       | 2023-10-29         |
| [`05-conditionals`](05-conditionals) |   Conditional statements    | 2023-11-05         |
| [`06-loops`](06-loops)               |            Loops            | 2023-11-12         |
| [`07-collections`](07-collections)   | Lists and other collections | 2023-11-19         |
| [`project`](project)                 |   Your own larger project   | 2023-11-19         |

**Note**: The table above contains suggested deadlines. The actual **deadline is 2023-11-19 23:59 CET!**

### Dependencies / Libraries

If you want to use external libraries for your large project, make sure to add the dependency to the [requirements.txt](requirements.txt) file, such that they can be installed via `pip install -r requirements.txt`.
Using external libraries is not required.

### Running the Projects

You can use the command `python project/main.py` to run your large projects (replace `project` with another folder name to run one of your smaller projects instead).

### Testing the Projects

You can use the command `pytest project` to test your projects (replace `project` with another folder name to test one of your smaller projects instead).
Don't worry if you don't see much output - `pytest` hides passed tests by default.
To show more information (including passed tests), use the command `pytest project -v` instead.

## Timesheet

Track your time investment for this lecture in the timesheet at the bottom of this document.

*Timesheet*:

|       Date | Start Time | End Time | Breaks | Cumulative Total Time | Description                                                                          |
|-----------:|-----------:|---------:|-------:|----------------------:|:-------------------------------------------------------------------------------------|
| 2023-10-03 |      19:00 |    22:00 |    000 |                003:00 | [Searching for inspiration](docs/2023-10-03.md)                                      |
| 2023-10-04 |      14:00 |    00:00 |    015 |                008:45 | [First prototype](docs/2023-10-04.md)                                                |
| 2023-10-05 |      10:00 |    13:00 |    000 |                011:45 | [Reimplementing the UI](docs/2023-10-05.md)                                          |
| 2023-10-06 |      15:00 |    20:00 |    105 |                015:00 | [Experimenting with neural networks](docs/2023-10-06.md)                             |
| 2023-10-07 |      15:00 |    17:00 |    000 |                017:00 | [Setting up GitLab](docs/2023-10-07.md)                                              |
| 2023-10-08 |      17:00 |    23:00 |    060 |                022:00 | [Preparing the layout](docs/2023-10-08.md)                                           |
| 2023-10-09 |      14:00 |    14:30 |    000 |                022:30 | [Using Icecream debugger](https://www.youtube.com/watch?v=JJ9zZ8cyaEk)               |
| 2023-10-13 |      09:30 |    16:30 |    300 |                024:30 | [Small improvements](docs/2023-10-13.md)                                             |
| 2023-10-15 |      16:00 |    21:00 |    060 |                028:30 | [Added API&AI Data](docs/2023-10-15.md)                                              |
| 2023-10-17 |      17:00 |    23:30 |    120 |                033:00 | [Worked on ML in Kaggle](docs/2023-10-17.md)                                         |
| 2023-10-24 |      15:00 |    17:00 |    000 |                035:00 | Meeting with the Data Team of the university to discuss about improving the ML model |
| 2023-10-25 |      09:00 |    17:00 |    120 |                041:00 | [Big refactoring](docs/2023-10-25.md)                                                |
| 2023-10-26 |      14:00 |    19:00 |    000 |                046:00 | [Continued refactoring](docs/2023-10-26.md)                                          |
| 2023-10-27 |      16:00 |    21:00 |    000 |                051:00 | Tried to transfer state from page to page -> Failed                                  |
| 2023-10-28 |      13:00 |    22:00 |    000 |                060:00 | [Changing UI framework](docs/2023-10-28.md)                                          |
| 2023-11-04 |      15:00 |    20:00 |    000 |                065:00 | Tried out various ML combinations on Kaggle                                          |
| 2023-11-05 |      17:00 |    23:00 |    060 |                070:00 | [Added Sourcery Tests](docs/2023-11-05.md)                                           |
| 2023-11-06 |      17:00 |    19:00 |    000 |                072:00 | Added some information to the application page and model                             |
| 2023-11-11 |      10:00 |    12:00 |    000 |                074:00 | Refactored some code, added docs                                                     |
| 2023-11-18 |      14:00 |    20:00 |    000 |                080:00 | [Finalized project](docs/2023-11-18.md)                                              |

