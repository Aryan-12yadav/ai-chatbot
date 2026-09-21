# Basic test placeholder. Full integration tests require an API key and a populated RAG index.
def test_project_structure():
    import os
    assert os.path.exists('app/main.py')
    assert os.path.exists('data/company_faq.txt')
