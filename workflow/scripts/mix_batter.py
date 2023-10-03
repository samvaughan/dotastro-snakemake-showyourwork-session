from pathlib import Path

smk = snakemake  # noqa

eggs = smk.input.eggs
flour = smk.input.flour
sugar = smk.input.sugar
vanilla_essence = smk.input.vanilla_essence

n_stirs = smk.params.number_of_stirs

for i in range(n_stirs):
    print(f"stir {i}!")

Path(smk.output.cake_batter).touch()
