[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/FAQgW8R_)
Develop **at least two** of the following exercises, using test-driven development techniques.

## Rover
We want to develop a class that models a rover that can move over the Moon's surface. It should support the following features:

* It should receive commands via a string on characters `R`, `L`, `U`, `D` - that encode respectively _move right_, _move left_, _move up_, _move down_ commands;

* Should throw an exception when moving in a certain direction _would hit an obstacle_;

* NASA tells us not to belittle the poor Rover; treat it as a serious system, modeling commands as strings is not enough. Refactor them as you believe it is appropriate.

* It should be possible to switch ``guide system``, enabling the rover to be guided by commands `R`, `L`, `F`, `W` - which now mean _rotate right 90°_, _rotate left 90°_, _go forward_, _go backward_;

* Draw a picture of the route the rover has currently followed.

## Password Validator
Your task is to create a simple password validator, as seen on many websites. The requirements are as follows:

* The password needs to be at least 8 characters long and at most 16 characters long
* The password needs to have at least an uppercase letter and a digiti
* The password needs at least 4 distinct characters
* The password can't contain adjacent characters
* Expose an API to let developers define custom validation behavior, such as support for regular expressions and filtering words that are too common
* Users should be notified _why_ a password is not valid, e.g. which validation criterion they are violating
* It should work with JSON input and CSV input, for multiple passwords submitted at the same time

## Template Engine
Your task is to develop a template engine that allows to generate text by replacing placeholder tokens from a text (``template'') with user-defined parameters. Here's an example:

```
Hey {$name}! You've won a prize!
```

By substituting `name` with `antonio`, we obtain the text:

```
Hey antonio! You've won a prize!
```

The proposed solution should also be able, given a template, to produce multiple texts based on parameters' assignments found on a JSON or CSV file.

## Circuit Simulator
Your task is to develop a simulator that is able to evaluate circuits composed of AND, OR and NOT gates. The simulator should parse the content of a file, which describes the cirrcuit, and evaluate it according to some values of the input gates. _You can assume the gates are listed in the ``correct order'' - without requiring to think about forward declaration for gates.

```
x_0 = Input()
x_1 = Input()
x_2 = And(x_0, x_1)
x_3 = Not(x_2)
x_4 = Output(x_3)
```

The `Output` gate is a gate which is used to query the state of other gates, echoing back its value. `Input` gates are evaluated according to user inputs (either `0` or `1`). `And`, `Or`, `Not` gates are evaluated as usual.
