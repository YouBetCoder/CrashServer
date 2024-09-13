from decimal import Decimal


def weighted_average(decimals: list[Decimal]) -> Decimal:
    """Calculates a weighted average of a list of decimals, where larger values have a smaller weight.

    Args:
        decimals: A list of decimal values.

    Returns:
        The weighted average of the decimals.
    """

    desired_average = Decimal(.1)  # Adjust this to your desired average
    weights = [Decimal(1) / (Decimal(abs(Decimal(decimal) - desired_average)) + Decimal(1)) for decimal in decimals]
    weighted_sum = sum(Decimal(decimal) * weight for decimal, weight in zip(decimals, weights))
    weighted_total = sum(weights)
    return weighted_sum / weighted_total
