# Part B: Reflection

### 1. How many tests did you write in Part A, and how many lines of production code? What is the ratio?
> In Part A, we wrote 8 test cases in `test_kitchen.py`, and our code in `kitchen.py` is about 48 lines long. The ratio of test code to actual code is almost 1:1. This shows how TDD helps keep our code short and clean, because we only write what is really needed to make our tests pass.

---

### 2. When was your bar red for the longest time, and what made it last so long?
> The test stayed red the longest during Step A6 when we started adding quantities with `Converter`. First, it failed with an `AttributeError` because `Quantity` didn't have the `plus` method yet. Then, we got an `ImportError` because we ran the test before saving the changes in `kitchen.py`. It took a few moments to make sure both files were properly connected and saved.

---

### 3. Find one place where you used Fake It, one where you triangulated, and one where you used Obvious Implementation. Looking back, was each choice right?
> - **Fake It:** In Step A6, we just hardcoded `return grams(500)` in `Converter.reduce` to get our first addition test to pass quickly.
> - **Triangulation:** We then added a second addition test using 100 g + 200 g = 300 g. This forced us to stop hardcoding and write real math (`augend.amount + addend.amount`).
> - **Obvious Implementation:** When writing `Converter.rate()`, returning 1 for the same unit and getting the rate from a dictionary for different units was very straightforward, so we wrote the real logic directly.
> 
> Looking back, these choices worked well. Faking made the first step easy, triangulation made sure our math actually worked, and obvious implementation saved time on simple logic.

---

### 4. Which items are still on your test list? Which would you implement next, and which should you delete because they were speculation?
> We completed everything on our main test list for Part A.
> - **Implement next:** We should handle what happens when a conversion rate is missing (like showing a clear error message), and maybe add subtraction.
> - **Delete / Speculation:** We should drop ideas like division between units or temperature conversion. They make things too complicated right now, and nobody asked for them yet.

---

### 5. Look at Quantity.reduce. If you had designed the whole system on paper first, would you have written this method?
> Probably not. If I planned it on paper first, I would have put all the conversion work inside `Converter` using `if/else` statements to check if the input is a single `Quantity` or a `Sum`. But following TDD step-by-step led us to put `reduce` inside both classes instead, which ended up being much simpler and cleaner without needing messy `if/else` checks.

---

### 6. In Part 0 you wrote the tests after the code, and in Part A before it. How did the two feel different, and which tests shaped your design?
> Writing tests after the code in Part 0 felt like doing a chore just to double-check my work. But writing tests first in Part A felt like building a blueprint; it forced me to think about how classes should look and behave before typing any logic. Two tests shaped our design the most: the multiplication test that forced us to treat `Quantity` as an immutable object, and the nested expression test `(200 g + 1 oz) * 2` that showed us how `Sum` and `Quantity` could work together.