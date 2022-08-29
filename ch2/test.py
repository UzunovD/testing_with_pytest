from cards import Card

def test_field_access():
    c = Card('some todo', 'Me', 'todo', 12)
    assert c.summary == 'some todo'
    assert c.owner == 'Me'
    assert c.state == 'todo'
    assert c.id == 12

def test_default():
    c = Card()
    assert c.summary is None
    assert c.owner is None
    assert c.state == 'todo'
    assert c.id is None

def test_equality():
    c1 = Card('some todo', 'Me', 'todo', 12)
    c2 = Card('some todo', 'Me', 'todo', 12)
    assert c1 == c2

def test_equality_with_diff_ids():
    c1 = Card('some todo', 'Me', 'todo', 13)
    c2 = Card('some todo', 'Me', 'todo', 12)
    assert c1 == c2

def test_inequality():
    c1 = Card('some todo', 'Me', 'todo', 13)
    c2 = Card('some todo', 'Me', 'done', 12)
    assert c1 != c2

def test_from_dict():
    dict_ ={'summary': 'some todo', 'owner':'Me', 'state': 'todo', 'id': 13}
    c1 = Card.from_dict(dict_)
    c2 = Card('some todo', 'Me', 'todo', 13)
    assert c1 == c2

def test_to_dict():
        dict_ ={'summary': 'some todo', 'owner':'Me', 'state': 'todo', 'id': 13}
        c1 = Card.from_dict(dict_)
        assert dict_ == c1.to_dict()

