"""
nullstools.mod

Модуль, содержащий главный класс Mod.

Как импортировать:
from nullstools import mod
"""
from . import types
import zipfile
import json
from pathlib import Path

class Mod:
    def __init__(self,
                 title: str | dict,
                 description: str | dict,
                 gv: int = None,
                 author: str | dict = None,
                 categories: list = None):
        """
        Класс Mod - основной класс для работы с модами

        :param title: Название мода
        :param description: Описание
        :param gv: Совместимая версия игры, без цифр после запятой, например 62
        :param author: Информация об авторе
        :param categories: Категории для библиотеки Null's Brawl

        title, description, и author поддерживают некоторые HTML-теги.
        """

        self.title = title
        self.description = description
        self.gv = gv
        self.author = author
        self.categories = categories

        self.campaign = types.Campaign()
        self.character_components_logic = types.CharacterComponentsLogic()
        self.game_mode_variations = types.GameModeVariations()
        self.vi = types.VI()
        self.battle_feats = types.BattleFeats()
        self.skin_confs = types.SkinConfs()
        self.mastery_reward_types = types.MasteryRewardTypes()
        self.texts_patch = types.TextsPatch()
        self.ms = types.MS()
        self.pl = types.PL()
        self.items = types.Items()
        self.kr = types.KR()
        self.intro_flows = types.IntroFlows()
        self.player_map_environments = types.PlayerMapEnvironments()
        self.enumerated_id_lists = types.EnumeratedIdLists()
        self.he = types.HE()
        self.contest_types = types.ContestTypes()
        self.alliance_league_ranks = types.AllianceLeagueRanks()
        self.animations = types.Animations()
        self.accessories = types.Accessories()
        self.characters = types.Characters()
        self.player_titles = types.PlayerTitles()
        self.event_modifiers = types.EventModifiers()
        self.gear_rarities = types.GearRarities()
        self.bp_purchase_popup = types.BpPurchasePopup()
        self.ad_placements = types.AdPlacements()
        self.resources = types.Resources()
        self.seasonal_skin_sections = types.SeasonalSkinSections()
        self.mastery_hero_confs = types.MasteryHeroConfs()
        self.skin_anim_sequences = types.SkinAnimSequences()
        self.club_piggy_types = types.ClubPiggyTypes()
        self.gear_boosts = types.GearBoosts()
        self.ranked_locations = types.RankedLocations()
        self.shop_items = types.ShopItems()
        self.visual_offer_groupings = types.VisualOfferGroupings()
        self.globals = types.Globals()
        self.sounds = types.Sounds()
        self.hints = types.Hints()
        self.chronos_asset_ids = types.ChronosAssetIds()
        self.maps = types.Maps()
        self.night_market_bundles = types.NightMarketBundles()
        self.progression_skin_details = types.ProgressionSkinDetails()
        self.emotes = types.Emotes()
        self.character_components_client = types.CharacterComponentsClient()
        self.fr = types.FR()
        self.name_colors = types.NameColors()
        self.tiles = types.Tiles()
        self.fame_tiers = types.FameTiers()
        self.effects = types.Effects()
        self.traits = types.Traits()
        self.nl = types.NL()
        self.billing_packages = types.BillingPackages()
        self.trophy_world_parts = types.TrophyWorldParts()
        self.player_frames = types.PlayerFrames()
        self.locales = types.Locales()
        self.bosses = types.Bosses()
        self.alliance_roles = types.AllianceRoles()
        self.cnt = types.CNT()
        self.shop_style_sets = types.ShopStyleSets()
        self.alliance_badges = types.AllianceBadges()
        self.texts = types.Texts()
        self.sprays = types.Sprays()
        self.it = types.IT()
        self.login_calendar_items = types.LoginCalendarItems()
        self.collabs = types.Collabs()
        self.faces = types.Faces()
        self.messages = types.Messages()
        self.particle_emitters = types.ParticleEmitters()
        self.skin_albums = types.SkinAlbums()
        self.ranked_ranks = types.RankedRanks()
        self.carryables = types.Carryables()
        self.catalog_collections = types.CatalogCollections()
        self.competitive_pass_tiers = types.CompetitivePassTiers()
        self.mastery_points = types.MasteryPoints()
        self.ru = types.RU()
        self.skills = types.Skills()
        self.availability_window = types.AvailabilityWindow()
        self.gear_levels = types.GearLevels()
        self.mastery_levels = types.MasteryLevels()
        self.cn = types.CN()
        self.id = types.ID()
        self.challenges = types.Challenges()
        self.skin_campaigns = types.SkinCampaigns()
        self.es = types.ES()
        self.de = types.DE()
        self.tr = types.TR()
        self.health_bars = types.HealthBars()
        self.collab_game_modes = types.CollabGameModes()
        self.skins = types.Skins()
        self.jp = types.JP()
        self.ranked_star_rewards = types.RankedStarRewards()
        self.class_archetypes = types.ClassArchetypes()
        self.skin_rarities = types.SkinRarities()
        self.trophy_season_reward_levels = types.TrophySeasonRewardLevels()
        self.music = types.Music()
        self.area_effects = types.AreaEffects()
        self.pricepoints = types.PricePoints()
        self.map_templates = types.MapTemplates()
        self.event_slots = types.EventSlots()
        self.client_globals = types.ClientGlobals()
        self.records = types.Records()
        self.emote_bundles = types.EmoteBundles()
        self.projectiles = types.Projectiles()
        self.ar = types.AR()
        self.milestones = types.Milestones()
        self.fi = types.FI()
        self.location_themes = types.LocationThemes()
        self.trophy_worlds = types.TrophyWorlds()
        self.local_notifications = types.LocalNotifications()
        self.shop_panel_layouts = types.ShopPanelLayouts()
        self.player_thumbnails = types.PlayerThumbnails()
        self.random_reward_containers = types.RandomRewardContainers()
        self.themes = types.Themes()
        self.status_effects = types.StatusEffects()
        self.color_gradients = types.ColorGradients()
        self.club_piggy_levels = types.ClubPiggyLevels()
        self.cards = types.Cards()
        self.credits = types.Credits()
        self.alliance_league_modes = types.AllianceLeagueModes()
        self.club_piggy_wins = types.ClubPiggyWins()
        self.tutorial = types.Tutorial()
        self.record_levels = types.RecordLevels()
        self.night_market_items = types.NightMarketItems()
        self.location_features = types.LocationFeatures()
        self.string_replacement = types.StringReplacement()
        self.pt = types.PT()
        self.th = types.TH()
        self.random_rewards = types.RandomRewards()
        self.regions = types.Regions()
        self.trophy_world_milestones = types.TrophyWorldMilestones()
        self.locations = types.Locations()

    def build(self,
              output_file: str,
              is_zip: bool = False,
              assets_dir: str = None
              ) -> None:
        """
        Собирает ваш мод в файл, который можно подписать в https://t.me/nb_mods для использования в игре
        :param output_file: Путь до выходного файла (.zip или .json)
        :param is_zip: Если True, то выходной файл будет .zip архивом, иначе .json
        :param assets_dir: Если выходной файл - .zip архив, содержимое данной папки будет добавлено в корень архива
        :return: None
        """
        output_json = {
            "@title": self.title,
            "@description": self.description
        }

        if self.author is not None:
            output_json["@author"] = self.author

        if self.gv is not None:
            output_json["@gv"] = self.gv

        if self.categories is not None:
            output_json["@categories"] = self.categories

        # Скопируем данные объекта
        data = self.__dict__.copy()

        # Удалим мета-теги
        for meta_tag in ("title", "description", "author", "gv", "categories"):
            data.pop(meta_tag, None)

        # Добавим остальные объекты, только если они не пустые
        for key, value in data.items():
            if hasattr(value, 'to_dict'):
                object_data = value.to_dict()
                if object_data:
                    output_json[key] = object_data

        if is_zip:
            with zipfile.ZipFile(output_file, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
                zipf.writestr("config.json", json.dumps(output_json, indent=2, ensure_ascii=False))

                if assets_dir:
                    assets_path = Path(assets_dir)
                    base_path = assets_path.parent
                    for file_path in assets_path.rglob("*"):
                        if file_path.is_file():
                            arcname = file_path.relative_to(base_path)
                            zipf.write(file_path, arcname)

        else:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(output_json, f, indent=2, ensure_ascii=False)



