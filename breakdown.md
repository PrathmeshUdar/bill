# Split a restaurant bill among friends

## Steps
1. Get the total, the number of people, and the tip percentage.
2. Check the inputs are valid numbers in a sensible range.
3. Add the tip to the total.
4. Divide the new total by the number of people.
5. Round each share to 2 decimals.
6. Handle the leftover penny so the shares add up to the total.
7. Show each person's share.

## Edge cases
1. **Zero people:** dividing by zero crashes, so reject it with a clear error.
2. **Negative people:** makes no sense, so reject it.
3. **Negative total:** makes no sense, so reject it.
4. **Total of 0:** everyone pays 0, which is valid.
5. **One person:** pays the whole bill including the tip.
6. **Rounding:** 10.00 / 3 = 3.333..., so three rounded shares add up to 9.99, not 10.00.
7. **Uneven shares:** someone ordered more. Decide whether to split equally or by item.
8. **Tip of 0%:** valid, so no tip is added.
9. **Negative tip:** reject it (or treat it as a discount; that is a requirements decision).
10. **Tip before or after the split:** the result can differ, so decide and state it.
11. **Non-number input:** "abc" as the total must give a clear error, not a crash.
12. **Huge amounts:** very large totals or many people should not lose accuracy.
13. **Float errors:** 0.1 + 0.2 is not exactly 0.3, so money should use whole cents or Decimal.
