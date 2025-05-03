from preprocessor import preprocess_text

def test_preprocess_text():
    input_text = "I didn't like the food, but the service was not bad!"
    output = preprocess_text(input_text)
    assert isinstance(output, str)
    assert "not" in output  # not should still be present
