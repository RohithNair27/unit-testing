

## 🚗 Lab: Testing the Autonomous Vehicle Speed Controller

### 🧭 Scenario

You are part of the software team developing a **speed controller** for an autonomous car.
This controller automatically adjusts throttle and braking to maintain safe speeds under different road and traffic conditions.

Your task is to:

1. **Design tests** using:
   * **Black-box testing** (based on input-output behavior)
   * **White-box testing** (based on internal logic)
   * **Category partition** and **boundary value analysis**
2. **Measure test coverage** and reason about test completeness.

### Functions Under Test

The functions under test (FUT) are implemented in the `speed_controller.py` module. The function `update_speed()` calculates the speed of the vehicle based on the speed limit, current road conditions, traffic density, and slope. The input parameters are defined as follows:

- `road_condition`: specifies if the road conditions are nominal or if there is a special condition that may impact how fast the vehicle should travel. This must be one of: `clear`, `wet`, or `icy` (as a string).
- `traffic_density`: based on traffic density, the speed will be increased or reduced. This value must be between `0` and `100`. If the traffic density is less than `50`, the speed is increased. Otherwise, the speed is reduced.
- `slope_angle`: specified the current degree of slope angle as a value between `-10` (downhill) and `+10` (uphill). The speed should be decreased if the vehicle is traveling downhill. It should be increased when traveling uphill.

In addition, the class `SpeedController` specifies a boolean flag `safety_value` that impact the execution of `update_speed()`. If that flag is set to `true`, the speed may never exceed `10mph` under the posted speed limit.

As part of this excercise, you will create test cases that provide some notion of coverage and confidence. Each test case must specify a value for each of the parameters.

---

## 🐥 Step 1 — Run your first test

Take a look around. You'll find the Function Under Test (FUT) `update_speed()` in the `speed_controller.py` module. That is the function for which you will be creating unit tests. More specifically, you will be writing test cases that call the FUT with different input parameters and assert the outcome of running that function.

You'll also find a test module `test_black_box.py`. It uses the built-in Pyhton `unittest` framework to run the tests. A simple test case has been implemented to illustrate how to implement test cases. It contains a simple test case that specified input values, expected output value, and executes the FUT. It then defines an assertion that compares the actual result with the expected result.  You can run that test using the following command:

```
python -m unittest test_black_box.py
```

It will provide an output that indicates how many tests have been run and how many have failed.

🤔 Do you see any test failures? If so, what do you have to do to fix that issue?

---

## 🔍 Step 2 — Analyze Inputs Using Category Partition

The following exercise ask you to generate a list of input values for each parameter described above. You will do so using a combination of black box and white box approaches. Each task will be specific about what input parameter you should be generating input values for and which approach to use. Once you have identified input values for all parameters, you will write test cases with these values.

In class, we learned that we need to identify categories by how they affect the output or behavior of the application. What are the categories for each of the parameters? What are example values in each category? For example, a categorization for a fictional parameter `temperature` could be as follows:

- `cold` (`temperature < 30`): 0, 10
- `mild` (`30 <= temperature <= 60`): 32, 49
- `warm` (`temperature > 60`): 70, 80

🎯 For this task, consider the description provided for the input parameters `safety_mode` and `road_condition`. Apply the category partition method based on the parameter descriptions provided above.

---

## 🧮 Step 3 — Derive Boundary Values

Boundary value analysis tries to find issues around the boundaries of the value space. In class we have learned about two types of boundary values:

- **Nominal boundary values**: boundary values that are valid in the context of the requirements (e.g., `min+`, `max-`)
- **Invalid boundary values**: boundary values that are outside the specific range for that parameter (e.g., `min-`, `max+`)

Use the boundary value analysis method to identify test inputs for the parameters `traffic_density` and `slope_angle`. Follow the instructions provided in class. Separate nominal values from the invalid values. When you write your test cases, you can only have one invalid parameter value for each test case.

---

## ⚫ Step 4 — Write black box tests

After the above exercise, you should have input values for each of the parameters that influence the behavior of the `update_speed()` function. You will now develop the test cases based on these input values.


### Create test case spreadsheet

First, create test cases in a spreadsheet. Create a spreadsheet in which the top row lists the parameters as shown below. Then, list the values for each parameter in the rows below. For now, only list the *nominal* values from the boundary value analysis.

You will also have to determine the output value for each test case. In practice, there are various ways of determining the expected output (e.g., requirements, SMEs, etc. - see class slides). For this task, you can take a look at the source code to determine what you believe the output value should be.


| speed_limit | safety_mode | road_condition | traffic_density | slope_angle | outcome |
|-------------|-------------|----------------|-----------------|-------------|---------|
| 60          | true        | clear          | 12              | -2          | 62      |
| 60          | true        | wet            | 44              | -2          | 58      |
| 60          | true        | icy            | 78              | 9           | 55      |
| ...         | ...         | ...            | ...             | ...         | ...     |


For now, we will ignore interactions between parameters. That means you do not need to generate permutations between values of different parameters.

### Implement test cases

Next, open `test_black_box.py` and implement `10` of the tests that you identified. Use the example test to guide you in implementing your tests. In each test, you will define input values, invoke the FUT, and then assert the expected output.

🤔 What bugs did you find, if any? If you did find bugs, note them down and fix them before continuing.

---

## ⚪ Step 5 — White-Box Test Design

So far, you generated test cases based on requirements only. That is one approach to achieve a notion of coverage and gain confidence in your test cases. In this task, you will switch to a white-box testing approach. Study the program flow of `update_speed()` and devise test cases that achieve `100%` statement coverage. Create a new module named `test_white_box.py`. Then start implementing test cases that you have identified by studying the source code.

🤔 Did you find any more bugs? Again, write them down and fix them before continuing.

---

## 📊 Step 6 — Measure Test Coverage

In the previous tasks, you identified white box tests with the goal to achieve `100%` statement coverage. But you have not actually formally checked if you achieved that coverage. The `coverage` library can be used to generate a coverage report. If you have installed the dependencies in `requirements.txt`, you will be able to run the following commands:

```bash
coverage run -m unittest test_white_box.py
coverage report -m
```

Example output:

```
Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
speed_controller.py      31     10    68%   15, 30, 32, 36, 42-45, 49, 51, 55
test_white_box.py         9      1    89%   12
---------------------------------------------------
TOTAL                    49     12    76%
```

If your test coverage is less than `100%`, modify your test cases until you achieve that goal. Use the `Missing` column to identify what statement has not been covered. Then add a test case that covers that statement.