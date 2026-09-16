# Exercises

One module per topic covered in `presentations/1_Python_Basics.py`. Each
file contains functions (or classes) with a `# TODO` and
`raise NotImplementedError(...)` in place of the implementation: fill
them in, then check your work with the matching file in `tests/`. If you
get stuck, `solutions/` has a worked implementation of every exercise here.

From the repo root, run the whole test suite with:

```bash
just test
```

or a single module (e.g. just the Lists exercises):

```bash
just test tests/test_lists.py
```

## Topics

| Topic | Module | Exercises |
|---|---|---|
| Variables & Types | `variables_types.py` | `get_type_name`, `swap_values`, `describe_person`, `is_same_type`, `most_common_type` |
| Numeric Operators | `numeric_operators.py` | `divmod_pair`, `is_even`, `average`, `power`, `gcd_manual`, `is_prime` |
| Boolean Operators | `boolean_operators.py` | `is_in_range`, `both_true`, `either_true`, `exactly_one`, `majority_vote`, `implies` |
| Strings | `strings.py` | `reverse_string`, `is_palindrome`, `count_vowels`, `title_case_words`, `format_greeting`, `is_anagram`, `run_length_encode` |
| Casting | `casting.py` | `to_int_safe`, `celsius_to_fahrenheit`, `parse_bool`, `parse_csv_row`, `safe_cast_all` |
| Lists | `lists.py` | `add_item`, `remove_duplicates`, `second_largest`, `flatten`, `chunk`, `rotate`, `merge_sorted` |
| Sets | `sets.py` | `unique_elements`, `common_elements`, `only_in_first`, `is_subset`, `symmetric_difference_manual`, `is_disjoint` |
| Tuples | `tuples.py` | `swap_tuple`, `first_and_last`, `pairs_to_dict`, `make_point`, `unzip`, `nested_tuple_sum` |
| Dictionaries | `dictionaries.py` | `get_or_default`, `merge_dicts`, `invert_dict`, `count_occurrences`, `group_by_length`, `deep_get` |
| Control Flow | `control_flow.py` | `classify_number`, `grade_from_score`, `describe_day`, `bmi_category`, `fizzbuzz` |
| Loops & Iterations | `loops.py` | `sum_up_to`, `factorial`, `find_first_multiple`, `filter_even`, `pair_names_ages`, `squares_comprehension`, `flatten_deep`, `moving_average` |
| Functions | `functions.py` | `safe_divide`, `apply_twice`, `make_counter`, `make_multiplier`, `memoize`, `compose` |
| Lambda Functions | `lambdas.py` | `sort_by_length`, `square_all`, `keep_positive`, `build_adder`, `sort_by_multiple_keys`, `reduce_product` |
| Generators | `generators.py` | `countdown`, `even_numbers`, `fibonacci`, `squares_generator_expr`, `sliding_window`, `take` |
| Classes | `classes.py` | `Rectangle`, `Animal`/`Dog` (inheritance), `Stack`, `BankAccount` |
| Error Handling | `error_handling.py` | `safe_int`, `require_non_negative`, `divide_with_report`, `validate_age`, `retry`, `validate_password` |

Some exercises in each module are a warm-up on the topic's basics; the
last one or two are deliberately harder, often combining the topic with
something from an earlier section (e.g. `moving_average` in Loops, or
`memoize`/`compose` in Functions).
