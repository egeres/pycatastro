from __future__ import annotations


class RC:
    """Referencia Catastral"""

    def __init__(
        self,
        finca: int,
        hoja_del_plano: str,
        local: str,
        caracteres_de_control: str,
    ) -> None:
        assert isinstance(finca, int)
        assert isinstance(hoja_del_plano, str)
        assert isinstance(local, str)
        assert isinstance(caracteres_de_control, str)

        # Ensure there is at least a letter in hoja_del_plano
        assert any(c.isalpha() for c in hoja_del_plano)

        self.finca = finca
        self.hoja_del_plano = hoja_del_plano
        self.local = local
        self.caracteres_de_control = caracteres_de_control

    @classmethod
    def from_string(cls, rc: str) -> RC:
        return cls(
            finca=int(rc[:7]),
            hoja_del_plano=rc[7:15],
            local=rc[15:17],
            caracteres_de_control=rc[17:],
        )

    def to_dict(self) -> dict[str, str | int]:
        return {
            "finca": self.finca,
            "hoja_del_plano": self.hoja_del_plano,
            "local": self.local,
            "caracteres_de_control": self.caracteres_de_control,
        }
