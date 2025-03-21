from nomad.config.models.plugins import SchemaPackageEntryPoint

#from pydantic import Field


class SinteringEntryPoint(SchemaPackageEntryPoint):

    def load(self):
        from nomad_sintering.schema_packages.sintering import m_package

        return m_package


sintering = SinteringEntryPoint(
    name='Sintering',
    description='Schema package for describing a sintering process.',
)
