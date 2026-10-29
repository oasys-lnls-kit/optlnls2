from optlnls2.__main__ import entrypoint


def test_entrypoint_output(capsys):
    entrypoint()

    captured = capsys.readouterr()
    assert "Hello world!" in captured.out
