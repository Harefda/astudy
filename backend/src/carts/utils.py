import enum


class CartErrorMessages(enum.Enum):
    CART_ALREADY_EXISTS_ERROR = "CART_ALREADY_EXISTS_ERROR"
    REQUEST_FIELDS_ERROR = "REQUEST_FIELDS_ERROR"


class WishlistErrorMessages(enum.Enum):
    WISHLIST_ALREADY_EXISTS_ERROR = "WISHLIST_ALREADY_EXISTS_ERROR"


class SavedForLaterErrorMessages(enum.Enum):
    SAVED_FOR_LATER_LIST_ALREADY_EXISTS_ERROR = "SAVED_FOR_LATER_LIST_ALREADY_EXISTS_ERROR"