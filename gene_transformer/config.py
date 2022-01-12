from pydantic import BaseSettings as _BaseSettings
from pathlib import Path
from typing import TypeVar, Type, Union, Optional, Dict, Any
import yaml
import json

_T = TypeVar("_T")

class BaseSettings(_BaseSettings):
    def dump_yaml(self, cfg_path):
        with open(cfg_path, mode="w") as fp:
            yaml.dump(json.loads(self.json()), fp, indent=4, sort_keys=False)

    @classmethod
    def from_yaml(cls: Type[_T], filename: Union[str, Path]) -> _T:
        with open(filename) as fp:
            raw_data = yaml.safe_load(fp)
        return cls(**raw_data)

class ModelSettings(BaseSettings):
    # logging settings
    wandb_active: bool = True
    wandb_project_name: str = "codon_transformer"
    checkpoint_dir: str = "codon_transformer"

    # data settings
    tokenizer_file: str = "tokenizer_files/codon_wordlevel_100vocab.json"
    train_file: str = "mdh_codon_spaces_full_train.txt"
    val_file: str = "mdh_codon_spaces_full_val.txt"
    test_file: str = "mdh_codon_spaces_full_test.txt"
    small_subset: bool = False

    # blast settings
    enable_blast: bool = True
    blast_validation_file: str = "blast_file.fasta"
    num_blast_seqs_per_gpu: int = 5

    # model settings
    use_pretrained: bool = True
    batch_size: int = 4
    training_steps: int = 500
    block_size: int = 512
    val_check_interval: int = 100
    accumulate_grad_batches: int = 4

    # generation settings
    generate_upon_completion: bool = True
    num_generated_seqs_per_gpu: int = 15

if __name__ == "__main__":
    settings = ModelSettings()
    settings.dump_yaml("settings_template.yaml")