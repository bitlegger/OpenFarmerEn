from dataclasses import dataclass
from datetime import timedelta


@dataclass
class Settings:
    path_logs: str
    chrome_data_dir: str
    url_db: str = None
    # Send the interval of the HTTP request
    req_interval = 3
    # Send the interval of the contract request (add a few seconds on the interval of the HTTP request)
    transact_interval = 1
    # Scan at least once per hour, even if there is no available crop, this can handle new crops after the last scan code
    max_scan_interval = timedelta(minutes=15)
    # Each time you scan for at least 10 seconds, even if it is wrong to sweep
    min_scan_interval = timedelta(seconds=10)


# User configuration parameters
class user_param:
    rpc_domain_list: list = []
    query_rpc_domain: str = None
    rpc_domain: str = None
    assets_domain: str = None
    assets_domain_list: list = []

    wax_account: str = None
    use_proxy: bool = True
    proxy: str = None

    build: bool = True
    mining: bool = True
    chicken: bool = True
    plant: bool = True
    cow: bool = True
    mbs: bool = True
    mbs_mint: bool = False
    # When the energy is not enough, it will restore so many energy, but do not exceed the maximum energy.
    recover_energy: int = 500

    withdraw: bool = True
    auto_deposit: bool = True
    sell_corn: bool = True
    sell_barley: bool = True
    sell_milk: bool = True
    sell_egg: bool = True
    auto_plant: bool = True
    min_energy: int = 50

    on_server: bool = False

    # How many materials remain in the account
    need_fww: int = 200
    need_fwf: int = 200
    need_fwg: int = 200
    # At least the quantity, three materials sum
    withdraw_min: int = 200

    remaining_corn_num: int = 0
    remaining_barley_num: int = 0
    remaining_milk_num: int = 0
    remaining_egg_num: int = 0

    barleyseed_num: int = 0
    cornseed_num: int = 0

    fww_min: int = 0
    deposit_fww: int = 0
    fwf_min: int = 0
    deposit_fwf: int = 0
    fwg_min: int = 0
    deposit_fwg: int = 0

    min_durability: int = 0

    # Automatic buy food
    buy_food: bool = False
    buy_food_num: int = 0
    # Automatically buy barley seeds
    buy_barley_seed: bool = False
    # Automatically buy corn seeds
    buy_corn_seed: bool = False
    breeding: bool = False

    @staticmethod
    def to_dict():
        return {
            "rpc_domain_list": user_param.rpc_domain_list,
            "rpc_domain": user_param.rpc_domain,
            "query_rpc_domain": user_param.query_rpc_domain,
            "assets_domain_list": user_param.assets_domain_list,
            "assets_domain": user_param.assets_domain,
            "wax_account": user_param.wax_account,
            "use_proxy": user_param.use_proxy,
            "proxy": user_param.proxy,
            "build": user_param.build,
            "mining": user_param.mining,
            "chicken": user_param.chicken,
            "plant": user_param.plant,
            "cow": user_param.cow,
            "mbs": user_param.mbs,
            "mbs_mint": user_param.mbs_mint,
            "recover_energy": user_param.recover_energy,
            "withdraw": user_param.withdraw,
            "auto_deposit": user_param.auto_deposit,
            "sell_corn": user_param.sell_corn,
            "sell_barley": user_param.sell_barley,
            "sell_milk": user_param.sell_milk,
            "sell_egg": user_param.sell_egg,
            "auto_plant": user_param.auto_plant,
            "min_energy": user_param.min_energy,
            "on_server": user_param.on_server,
            "need_fww": user_param.need_fww,
            "need_fwf": user_param.need_fwf,
            "need_fwg": user_param.need_fwg,
            "withdraw_min": user_param.withdraw_min,
            "remaining_corn_num": user_param.remaining_corn_num,
            "remaining_barley_num": user_param.remaining_barley_num,
            "remaining_milk_num": user_param.remaining_milk_num,
            "remaining_egg_num": user_param.remaining_egg_num,
            "barleyseed_num": user_param.barleyseed_num,
            "cornseed_num": user_param.cornseed_num,
            "fww_min": user_param.fww_min,
            "deposit_fww": user_param.deposit_fww,
            "fwf_min": user_param.fwf_min,
            "deposit_fwf": user_param.deposit_fwf,
            "fwg_min": user_param.fwg_min,
            "deposit_fwg": user_param.deposit_fwg,
            "min_durability": user_param.min_durability,

            "buy_food": user_param.buy_food,
            "buy_food_num": user_param.buy_food_num,
            "buy_barley_seed": user_param.buy_barley_seed,
            "buy_corn_seed": user_param.buy_corn_seed,
            "breeding": user_param.breeding,
        }


def load_user_param(user: dict):
    user_param.rpc_domain_list = user.get("rpc_domain_list", ['https://api.wax.alohaeos.com'])
    user_param.rpc_domain = user.get("rpc_domain", 'https://api.wax.alohaeos.com')
    user_param.query_rpc_domain = user.get("query_rpc_domain", 'https://api.wax.alohaeos.com')
    user_param.assets_domain_list = user.get("assets_domain_list", ['https://wax.api.atomicassets.io'])
    user_param.assets_domain = user.get("assets_domain", 'https://wax.api.atomicassets.io')

    user_param.wax_account = user["wax_account"]
    user_param.use_proxy = user.get("use_proxy", True)
    user_param.proxy = user.get("proxy", None)
    user_param.build = user.get("build", True)
    user_param.mining = user.get("mining", True)
    user_param.chicken = user.get("chicken", True)
    user_param.cow = user.get("cow", True)
    user_param.plant = user.get("plant", True)
    user_param.mbs = user.get("mbs", True)
    user_param.mbs_mint = user.get("mbs_mint", False)
    user_param.sell_corn = user.get("sell_corn", False)
    user_param.sell_barley = user.get("sell_barley", False)
    user_param.sell_milk = user.get("sell_milk", False)
    user_param.sell_egg = user.get("sell_egg", False)
    user_param.auto_plant = user.get("auto_plant", False)
    user_param.recover_energy = user.get("recover_energy", 500)
    user_param.min_energy = user.get("min_energy", 50)
    user_param.min_durability = user.get("min_durability", 0)
    user_param.withdraw = user.get("withdraw", False)
    user_param.auto_deposit = user.get("auto_deposit", False)
    user_param.need_fww = user.get("need_fww", 200)
    user_param.need_fwf = user.get("need_fwf", 200)
    user_param.need_fwg = user.get("need_fwg", 200)
    user_param.withdraw_min = user.get("withdraw_min", 200)
    user_param.remaining_corn_num = user.get("remaining_corn_num", 0)
    user_param.remaining_barley_num = user.get("remaining_barley_num", 0)
    user_param.remaining_milk_num = user.get("remaining_milk_num", 0)
    user_param.remaining_egg_num = user.get("remaining_egg_num", 0)

    user_param.barleyseed_num = user.get("barleyseed_num", 0)
    user_param.cornseed_num = user.get("cornseed_num", 0)

    user_param.fww_min = user.get("fww_min", 0)
    user_param.deposit_fww = user.get("deposit_fww", 0)
    user_param.fwf_min = user.get("fwf_min", 0)
    user_param.deposit_fwf = user.get("deposit_fwf", 0)
    user_param.fwg_min = user.get("fwg_min", 0)
    user_param.deposit_fwg = user.get("deposit_fwg", 0)

    user_param.buy_food = user.get("buy_food", False)
    user_param.buy_food_num = user.get("buy_food_num", 0)
    user_param.buy_barley_seed = user.get("buy_barley_seed", False)
    user_param.buy_corn_seed = user.get("buy_corn_seed", False)
    user_param.breeding = user.get("breeding", False)


cfg = Settings(
    path_logs="./logs/",
    chrome_data_dir="./data_dir/",
)
