import pandas as pd
import numpy as np

gene_df = pd.DataFrame(
    [
        ['geneA', 'AKSJAFÖLKSJAFSDKLFJASÖLDKFA______________________'],
        ['geneB', 'asldkfÖSKDFJASLKDFSDFLKASJDFASDLFKJASDFKAÖDSF____'],
        ['geneC', 'ÖLASKJFSDLÖAFKJSFLSKDFLSDKFKDSFJSDJDF__LKSJDFLSDF']
    ],
    columns=['gene_name', 'sequence']
)

user_df = pd.DataFrame(
    [
        ['Tim', '', 'timddddddd@gmail.com'],
        ['Struppi', '', 'alkdsf@slkdfjs.com']
    ],
    columns=['name', 'email']
)


selection_df = pd.DataFrame(
    np.asarray([[11, 1], [12, 1], [13, 3]]),
    columns=['selection_nr', 'selection_owner_id']
)
selection_df = selection_df.convert_dtypes()