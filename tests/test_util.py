"""Util tests."""
from custom_components.steam_wishlist.util import get_steam_game


def test_get_steam_game_unreleased_game() -> None:
    """Test that we get the correct return value for an unreleased game."""
    game_id = "12007070"
    game = {
        "name": "Deathground",
        "capsule": f"https://cdn.akamai.steamstatic.com/steam/apps/{game_id}/header_292x136.jpg?t=1680256324",
        "review_score": 0,
        "review_desc": "No user reviews",
        "reviews_total": "0",
        "reviews_percent": 0,
        "release_date": 1684421117,
        "release_string": "Coming soon",
        "platform_icons": "",
        "subs": [],
        "type": "Game",
        "screenshots": [],
        "review_css": "no_reviews",
        "priority": 0,
        "added": 1598977652,
        "background": "",
        "rank": 1000,
        "tags": [],
        "is_free_game": False,
        "deck_compat": 0,
        "prerelease": 1,
        "win": 1,
    }
    actual = get_steam_game(game_id, game)
    expected = {
        "airdate": 1684421117,
        "deep_link": f"https://store.steampowered.com/app/{game_id}",
        "fanart": f"https://cdn.akamai.steamstatic.com/steam/apps/{game_id}/header_292x136.jpg?t=1680256324",
        "genres": "",
        "box_art_url": f"https://cdn.akamai.steamstatic.com/steam/apps/{game_id}/header_292x136.jpg?t=1680256324",
        "normal_price": None,
        "percent_off": 0,
        "rating": "Reviews:&nbsp;&nbsp;0% (No user reviews)",
        "poster": f"https://cdn.akamai.steamstatic.com/steam/apps/{game_id}/header_292x136.jpg?t=1680256324",
        "price": "Price:&nbsp;&nbsp;TBD",
        "release": "Released:&nbsp;&nbsp;May 18, 2023",
        "review_desc": "No user reviews",
        "reviews_percent": 0,
        "reviews_total": "0",
        "sale_price": None,
        "steam_id": game_id,
        "title": "Deathground",
    }
    assert expected == actual


def test_get_steam_game_with_sale_price() -> None:
    """Test that we get the correct return value for a normal on sale game."""
    game_id = "1262350"
    game = {
        "name": "SIGNALIS",
        "capsule": f"https://cdn.akamai.steamstatic.com/steam/apps/{game_id}/header_292x136.jpg?t=1684085470",
        "review_score": 9,
        "review_desc": "Overwhelmingly Positive",
        "reviews_total": "6,844",
        "reviews_percent": 97,
        "release_date": 1666879183,
        "release_string": "Oct 27, 2022",
        "platform_icons": "",
        "subs": [
            {
                "packageid": 438763,
                "bundleid": None,
                "discount_block": "",
                "discount_pct": 20,
                "price": "1599",
            }
        ],
        "type": "Game",
        "screenshots": [],
        "review_css": "positive",
        "priority": 0,
        "added": 1669934204,
        "background": "",
        "rank": 558,
        "tags": [],
        "is_free_game": False,
        "deck_compat": "3",
        "win": 1,
    }
    actual = get_steam_game(game_id, game)
    expected = {
        "airdate": 1666879183,
        "deep_link": f"https://store.steampowered.com/app/{game_id}",
        "fanart": f"https://cdn.akamai.steamstatic.com/steam/apps/{game_id}/header_292x136.jpg?t=1684085470",
        "genres": "",
        "box_art_url": f"https://cdn.akamai.steamstatic.com/steam/apps/{game_id}/header_292x136.jpg?t=1684085470",
        "normal_price": 19.99,
        "percent_off": 20,
        "poster": f"https://cdn.akamai.steamstatic.com/steam/apps/{game_id}/header_292x136.jpg?t=1684085470",
        "price": "1̶9̶.̶9̶9 $15.99 (20% off)&nbsp;&nbsp;🎫",
        "rating": "Reviews:&nbsp;&nbsp;97% (Overwhelmingly Positive)",
        "release": "Released:&nbsp;&nbsp;Oct 27, 2022",
        "review_desc": "Overwhelmingly Positive",
        "reviews_percent": 97,
        "reviews_total": "6,844",
        "sale_price": 15.99,
        "steam_id": game_id,
        "title": "SIGNALIS",
    }
    assert expected == actual


def test_get_steam_game_with_100_percent_discount() -> None:
    """Test that a free game doesn't cause a division by zero error."""
    game_id = "1262350"
    game = {
        "name": "SIGNALIS",
        "capsule": f"https://cdn.akamai.steamstatic.com/steam/apps/{game_id}/header_292x136.jpg?t=1684085470",
        "review_score": 9,
        "review_desc": "Overwhelmingly Positive",
        "reviews_total": "6,844",
        "reviews_percent": 97,
        "release_date": 1666879183,
        "release_string": "Oct 27, 2022",
        "platform_icons": "",
        "subs": [
            {
                "packageid": 438763,
                "bundleid": None,
                "discount_block": "",
                "discount_pct": 100,
                "price": "0",
            }
        ],
        "type": "Game",
        "screenshots": [],
        "review_css": "positive",
        "priority": 0,
        "added": 1669934204,
        "background": "",
        "rank": 558,
        "tags": [],
        "is_free_game": False,
        "deck_compat": "3",
        "win": 1,
    }
    actual = get_steam_game(game_id, game)
    expected = {
        "airdate": 1666879183,
        "deep_link": f"https://store.steampowered.com/app/{game_id}",
        "fanart": f"https://cdn.akamai.steamstatic.com/steam/apps/{game_id}/header_292x136.jpg?t=1684085470",
        "genres": "",
        "box_art_url": f"https://cdn.akamai.steamstatic.com/steam/apps/{game_id}/header_292x136.jpg?t=1684085470",
        "normal_price": 0,
        "percent_off": 100,
        "poster": f"https://cdn.akamai.steamstatic.com/steam/apps/{game_id}/header_292x136.jpg?t=1684085470",
        "price": "Price:&nbsp;&nbsp;TBD",
        "rating": "Reviews:&nbsp;&nbsp;97% (Overwhelmingly Positive)",
        "release": "Released:&nbsp;&nbsp;Oct 27, 2022",
        "review_desc": "Overwhelmingly Positive",
        "reviews_percent": 97,
        "reviews_total": "6,844",
        "sale_price": 0.0,
        "steam_id": game_id,
        "title": "SIGNALIS",
    }
    assert expected == actual
