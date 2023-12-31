######## snakemake preamble start (automatically inserted, do not edit) ########
import sys

sys.path.extend(
    [
        "/Users/samvaughan/software/mambaforge/envs/py-science/lib/python3.11/site-packages",
        "/Users/samvaughan/Library/Caches/snakemake/snakemake/source-cache/runtime-cache/tmp9z1vjrtb/file/Users/samvaughan/Science/Misc/dotAstro12/Snakemake_intro/workflow/scripts",
        "/Users/samvaughan/Science/Misc/dotAstro12/Snakemake_intro/workflow/scripts",
    ]
)
import pickle

snakemake = pickle.loads(
    b"\x80\x04\x95\xf2\x04\x00\x00\x00\x00\x00\x00\x8c\x10snakemake.script\x94\x8c\tSnakemake\x94\x93\x94)\x81\x94}\x94(\x8c\x05input\x94\x8c\x0csnakemake.io\x94\x8c\nInputFiles\x94\x93\x94)\x81\x94(\x8c\x15results/eggs.prepared\x94\x8c\x16results/flour.prepared\x94\x8c\x16results/sugar.prepared\x94\x8c$resources/vanilla_essence.ingredient\x94e}\x94(\x8c\x06_names\x94}\x94(\x8c\x04eggs\x94K\x00N\x86\x94\x8c\x05flour\x94K\x01N\x86\x94\x8c\x05sugar\x94K\x02N\x86\x94\x8c\x0fvanilla_essence\x94K\x03N\x86\x94u\x8c\x12_allowed_overrides\x94]\x94(\x8c\x05index\x94\x8c\x04sort\x94eh\x1b\x8c\tfunctools\x94\x8c\x07partial\x94\x93\x94h\x06\x8c\x19Namedlist._used_attribute\x94\x93\x94\x85\x94R\x94(h!)}\x94\x8c\x05_name\x94h\x1bsNt\x94bh\x1ch\x1fh!\x85\x94R\x94(h!)}\x94h%h\x1csNt\x94bh\x11h\nh\x13h\x0bh\x15h\x0ch\x17h\rub\x8c\x06output\x94h\x06\x8c\x0bOutputFiles\x94\x93\x94)\x81\x94\x8c\x13results/cake.batter\x94a}\x94(h\x0f}\x94\x8c\x0bcake_batter\x94K\x00N\x86\x94sh\x19]\x94(h\x1bh\x1ceh\x1bh\x1fh!\x85\x94R\x94(h!)}\x94h%h\x1bsNt\x94bh\x1ch\x1fh!\x85\x94R\x94(h!)}\x94h%h\x1csNt\x94bh2h/ub\x8c\x06params\x94h\x06\x8c\x06Params\x94\x93\x94)\x81\x94Kda}\x94(h\x0f}\x94\x8c\x0fnumber_of_stirs\x94K\x00N\x86\x94sh\x19]\x94(h\x1bh\x1ceh\x1bh\x1fh!\x85\x94R\x94(h!)}\x94h%h\x1bsNt\x94bh\x1ch\x1fh!\x85\x94R\x94(h!)}\x94h%h\x1csNt\x94bhCKdub\x8c\twildcards\x94h\x06\x8c\tWildcards\x94\x93\x94)\x81\x94}\x94(h\x0f}\x94h\x19]\x94(h\x1bh\x1ceh\x1bh\x1fh!\x85\x94R\x94(h!)}\x94h%h\x1bsNt\x94bh\x1ch\x1fh!\x85\x94R\x94(h!)}\x94h%h\x1csNt\x94bub\x8c\x07threads\x94K\x01\x8c\tresources\x94h\x06\x8c\tResources\x94\x93\x94)\x81\x94(K\x01K\x01\x8c0/var/folders/5r/wxyz8ntn6ks8g2wwjv0qrszc0000gq/T\x94e}\x94(h\x0f}\x94(\x8c\x06_cores\x94K\x00N\x86\x94\x8c\x06_nodes\x94K\x01N\x86\x94\x8c\x06tmpdir\x94K\x02N\x86\x94uh\x19]\x94(h\x1bh\x1ceh\x1bh\x1fh!\x85\x94R\x94(h!)}\x94h%h\x1bsNt\x94bh\x1ch\x1fh!\x85\x94R\x94(h!)}\x94h%h\x1csNt\x94bheK\x01hgK\x01hihbub\x8c\x03log\x94h\x06\x8c\x03Log\x94\x93\x94)\x81\x94}\x94(h\x0f}\x94h\x19]\x94(h\x1bh\x1ceh\x1bh\x1fh!\x85\x94R\x94(h!)}\x94h%h\x1bsNt\x94bh\x1ch\x1fh!\x85\x94R\x94(h!)}\x94h%h\x1csNt\x94bub\x8c\x06config\x94}\x94\x8c\x04rule\x94\x8c\x0cmix_together\x94\x8c\x0fbench_iteration\x94N\x8c\tscriptdir\x94\x8cJ/Users/samvaughan/Science/Misc/dotAstro12/Snakemake_intro/workflow/scripts\x94ub."
)
from snakemake.logging import logger

logger.printshellcmds = False
__real_file__ = __file__
__file__ = "/Users/samvaughan/Science/Misc/dotAstro12/Snakemake_intro/workflow/scripts/mix_batter.py"
######## snakemake preamble end #########
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
