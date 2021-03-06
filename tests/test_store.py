from moban.core.definitions import TemplateTarget
from moban.core.mobanfile.store import Store


def test_store():
    store = Store()
    output = "output"
    target = TemplateTarget("template_file", "data_file", output)
    store.add(target)
    assert target == store.look_up_by_output.get(output)
