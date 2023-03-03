import enum


class BillingProfileErrorMessages(enum.Enum):
    BILLING_PROFILE_ALREADY_EXISTS_ERROR = "BILLING_PROFILE_ALREADY_EXISTS_ERROR"


class CardErrorMessages(enum.Enum):
    WRONG_CARD_STRIPE_ID_ERROR = "WRONG_CARD_STRIPE_ID_ERROR"
    WRONG_CARD_BRAND_ERROR = "WRONG_CARD_BRAND_ERROR"
    WRONG_CARD_LAST4_ERROR = "WRONG_CARD_LAST4_ERROR"