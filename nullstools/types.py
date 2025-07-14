from typing import Any

class NullObject:
    """
    Используется для указания, что этого параметра быть не должно в выходном .json
    """
    pass

class BaseObject:
    def to_dict(self):
        result = {}

        for attr, value in self.__dict__.items():
            if isinstance(value, NullObject):
                continue

            if isinstance(value, dict):
                clean_dict = {
                    k: v for k, v in value.items()
                    if not isinstance(v, NullObject)
                }
                if clean_dict:
                    result[attr] = clean_dict
            else:
                result[attr] = value

        return result

    def add_object(self, **kwargs):
        if not kwargs:
            return

        to_remove = [k for k in kwargs if k.startswith("__")]
        for k in to_remove:
            kwargs.pop(k)

        key = next(iter(kwargs))
        name_value = kwargs.pop(key)

        self.__setattr__(name_value, kwargs)


class Campaign(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   TID: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')

        super().add_object(**data)


class CharacterComponentsLogic(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Type: str | list[str] = NullObject(),
                   Values: int | list[int] = NullObject(),
                   Projectiles: str | list[str] = NullObject(),
                   AreaEffects: str | list[str] = NullObject(),
                   Characters: str | list[str] = NullObject(),
                   Skills: str | list[str] = NullObject(),
                   StatusEffects: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class GameModeVariations(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Variation: int | list[int] = NullObject(),
                   Disabled: bool | list[bool] = NullObject(),
                   ShortName: str | list[str] = NullObject(),
                   TID: str | list[str] = NullObject(),
                   ChatSuggestionItemName: str | list[str] = NullObject(),
                   GameModeRoomIconName: str | list[str] = NullObject(),
                   GameModeIconName: str | list[str] = NullObject(),
                   BannerOverrideSWF: str | list[str] = NullObject(),
                   BannerOverrideExportName: str | list[str] = NullObject(),
                   SquareBannerOverrideSWF: str | list[str] = NullObject(),
                   SquareBannerOverrideExportName: str | list[str] = NullObject(),
                   MaxScore: int | list[int] = NullObject(),
                   ScoreSfx: str | list[str] = NullObject(),
                   OpponentScoreSfx: str | list[str] = NullObject(),
                   ScoreText: str | list[str] = NullObject(),
                   ScoreOpponentText: str | list[str] = NullObject(),
                   ScoreTextEnd: str | list[str] = NullObject(),
                   ScoreOpponentTextEnd: str | list[str] = NullObject(),
                   ScoreVO: str | list[str] = NullObject(),
                   OpponentScoreVO: str | list[str] = NullObject(),
                   VictoryVO: str | list[str] = NullObject(),
                   DefeatVO: str | list[str] = NullObject(),
                   DoubleTakedownVO: str | list[str] = NullObject(),
                   TripleTakedownVO: str | list[str] = NullObject(),
                   QuadTakedownVO: str | list[str] = NullObject(),
                   TeamTakedownVO: str | list[str] = NullObject(),
                   FirstBloodVO: str | list[str] = NullObject(),
                   PointsLeftMediumVO: str | list[str] = NullObject(),
                   PointsLeftLowVO: str | list[str] = NullObject(),
                   FriendlyMenuOrder: int | list[int] = NullObject(),
                   IntroText: str | list[str] = NullObject(),
                   IntroDescText: str | list[str] = NullObject(),
                   IntroDescText2: str | list[str] = NullObject(),
                   OvertimeText: str | list[str] = NullObject(),
                   OvertimeVO: str | list[str] = NullObject(),
                   PlayerCountInfo: str | list[str] = NullObject(),
                   StartNotification: str | list[str] = NullObject(),
                   EndNotification: str | list[str] = NullObject(),
                   Color: str | list[str] = NullObject(),
                   BgColor: str | list[str] = NullObject(),
                   FallbackPlayerMapEnvironment: str | list[str] = NullObject(),
                   TeamEntryItemName: str | list[str] = NullObject(),
                   PanelTeamOnlineName: str | list[str] = NullObject(),
                   SpecificEmote1: str | list[str] = NullObject(),
                   SpecificEmote2: str | list[str] = NullObject(),
                   SpecificEmote3: str | list[str] = NullObject(),
                   ScorePanelIconFrame: int | list[int] = NullObject(),
                   HasModeSpecificQuest: bool | list[bool] = NullObject(),
                   MaxDamage: int | list[int] = NullObject(),
                   MaxHealing: int | list[int] = NullObject(),
                   CustomValue1: int | list[int] = NullObject(),
                   PlayerCollectBountyStars: bool | list[bool] = NullObject(),
                   PlayersCollectPowerCubes: bool | list[bool] = NullObject(),
                   MaxPowerCubesToDrop: int | list[int] = NullObject(),
                   PlayersCollectBolts: bool | list[bool] = NullObject(),
                   ItemClaimDelaySeconds: int | list[int] = NullObject(),
                   IsPlayedOnVeryLargeMap: bool | list[bool] = NullObject(),
                   SpectateAfterGameOver: bool | list[bool] = NullObject(),
                   SpectateAfterDeath: bool | list[bool] = NullObject(),
                   SpectateFriendAfterDeath: bool | list[bool] = NullObject(),
                   HasCornerScoreNumbers: bool | list[bool] = NullObject(),
                   HasCornerScoreForBothTeams: bool | list[bool] = NullObject(),
                   IsBattleRoyale: bool | list[bool] = NullObject(),
                   HasAntiTeamingFeatures: bool | list[bool] = NullObject(),
                   HasBoxesWithPowerCubes: bool | list[bool] = NullObject(),
                   HasOffScreenIndicator: bool | list[bool] = NullObject(),
                   HasOffScreenBossIndicator: bool | list[bool] = NullObject(),
                   IsCoop: bool | list[bool] = NullObject(),
                   HasDownwardsTickingClock: bool | list[bool] = NullObject(),
                   DisplayOneHealthbar: bool | list[bool] = NullObject(),
                   DisplayOneHealthbarForBothTeams: bool | list[bool] = NullObject(),
                   DisplayOneBlueHealthbar: bool | list[bool] = NullObject(),
                   DisplayHealthbarForBothTeams: bool | list[bool] = NullObject(),
                   HealthbarsAreInOneCorner: bool | list[bool] = NullObject(),
                   HealthBarsFillUp: bool | list[bool] = NullObject(),
                   HasTwoBases: bool | list[bool] = NullObject(),
                   IsSoloModeWithRespawns: bool | list[bool] = NullObject(),
                   IsSoloMode: bool | list[bool] = NullObject(),
                   GetHeroSelectionCount: int | list[int] = NullObject(),
                   HasTimerAndCanEndBeforeTimerRunsOut: bool | list[bool] = NullObject(),
                   ShouldSpawnCloseToTeammate: bool | list[bool] = NullObject(),
                   HasSpawnProtectionInTheStart: bool | list[bool] = NullObject(),
                   GiveMVPAtGameEnd: bool | list[bool] = NullObject(),
                   HasWinBasedExp: bool | list[bool] = NullObject(),
                   PanCameraToCenterWhenGameOver: bool | list[bool] = NullObject(),
                   RevealMapWhenGameOver: bool | list[bool] = NullObject(),
                   FlashHealthBar: bool | list[bool] = NullObject(),
                   IsGoalBasedMode: bool | list[bool] = NullObject(),
                   ShowTextOnScore: bool | list[bool] = NullObject(),
                   ModeHasCarryables: bool | list[bool] = NullObject(),
                   AllowAttackWhileCarrying: bool | list[bool] = NullObject(),
                   IsHorizontalMode: bool | list[bool] = NullObject(),
                   BattleTicks: int | list[int] = NullObject(),
                   HasOvertime: bool | list[bool] = NullObject(),
                   OvertimeHasGoldenGoal: bool | list[bool] = NullObject(),
                   RespawnSeconds: int | list[int] = NullObject(),
                   ModeHasSecondaryRespawnPoints: bool | list[bool] = NullObject(),
                   ModeGameObjectCount: int | list[int] = NullObject(),
                   RoundResetsWhenObjectiveIsMissing: bool | list[bool] = NullObject(),
                   DroppedItemOnDeath: str | list[str] = NullObject(),
                   BotGoalAreaEffect: str | list[str] = NullObject(),
                   BotItemPickup: str | list[str] = NullObject(),
                   BotItemPickup2: str | list[str] = NullObject(),
                   BotItemPickupRadius: int | list[int] = NullObject(),
                   HasTeamItems: bool | list[bool] = NullObject(),
                   PreventWallsOnBase: bool | list[bool] = NullObject(),
                   HasMultipleDifficulties: bool | list[bool] = NullObject(),
                   IsTypeOfBossFight: bool | list[bool] = NullObject(),
                   IsSpecialEvent: bool | list[bool] = NullObject(),
                   IsBlockedFromFriendlyRoom: bool | list[bool] = NullObject(),
                   AreTeamsDisabledIn: bool | list[bool] = NullObject(),
                   BossCharacterData: str | list[str] = NullObject(),
                   NumberOfRounds: int | list[int] = NullObject(),
                   MoveDeathNotificationsDown: bool | list[bool] = NullObject(),
                   ModeCarryable: str | list[str] = NullObject(),
                   TeamSize: int | list[int] = NullObject(),
                   TeamCount: int | list[int] = NullObject(),
                   ModeHasFillingPoison: bool | list[bool] = NullObject(),
                   BattleLoad: int | list[int] = NullObject(),
                   BattleLoadCoop: int | list[int] = NullObject(),
                   HasTokensToHold: bool | list[bool] = NullObject(),
                   IsMatchmakingBasedOnAverageHeroScore: bool | list[bool] = NullObject(),
                   IsNotRewardingTrophies: bool | list[bool] = NullObject(),
                   IsAllowDuplicateHeroes: bool | list[bool] = NullObject(),
                   TrophyGainedMultiplierPercent: int | list[int] = NullObject(),
                   BattleMusicOverride: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class VI(BaseObject):
    def add_object(self,
                   TID: str | list[str],
                   VI: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class BattleFeats(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   TID: str | list[str] = NullObject(),
                   Gradient: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class SkinConfs(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Character: str | list[str] = NullObject(),
                   Model: str | list[str] = NullObject(),
                   ModelCNOverride: str | list[str] = NullObject(),
                   GadgetModel: str | list[str] = NullObject(),
                   BigHeroIconOverrideSWF: str | list[str] = NullObject(),
                   BigHeroIconOverrideExportName: str | list[str] = NullObject(),
                   SmallHeroIconOverrideSWF: str | list[str] = NullObject(),
                   SmallHeroIconOverrideExportName: str | list[str] = NullObject(),
                   PortraitCameraFile: str | list[str] = NullObject(),
                   MirrorIntro: bool | list[bool] = NullObject(),
                   IdleAnim: str | list[str] = NullObject(),
                   WalkAnim: str | list[str] = NullObject(),
                   PrimarySkillAnim: str | list[str] = NullObject(),
                   SecondarySkillAnim: str | list[str] = NullObject(),
                   OverchargedSecondarySkillAnim: str | list[str] = NullObject(),
                   PrimarySkillRecoilAnim: str | list[str] = NullObject(),
                   PrimarySkillRecoilAnim2: str | list[str] = NullObject(),
                   SecondarySkillRecoilAnim: str | list[str] = NullObject(),
                   SecondarySkillRecoilAnim2: str | list[str] = NullObject(),
                   ReloadingAnim: str | list[str] = NullObject(),
                   PushbackAnim: str | list[str] = NullObject(),
                   DeployAnim: str | list[str] = NullObject(),
                   HappyAnim: str | list[str] = NullObject(),
                   HappyLoopAnim: str | list[str] = NullObject(),
                   RecruitRoadOverrideAnim: str | list[str] = NullObject(),
                   SadAnim: str | list[str] = NullObject(),
                   SadLoopAnim: str | list[str] = NullObject(),
                   LobbyAnim: str | list[str] = NullObject(),
                   LobbyLoopAnim: str | list[str] = NullObject(),
                   HeroScreenIdleAnim: str | list[str] = NullObject(),
                   HeroScreenAnim: str | list[str] = NullObject(),
                   HeroScreenLoopAnim: str | list[str] = NullObject(),
                   SignatureAnim: str | list[str] = NullObject(),
                   GachaOverrideAnim: str | list[str] = NullObject(),
                   HappyEnterAnim: str | list[str] = NullObject(),
                   SadEnterAnim: str | list[str] = NullObject(),
                   ProfileAnim: str | list[str] = NullObject(),
                   ShopGroupProfileAnim: str | list[str] = NullObject(),
                   BrawlPassPopupProfileAnim: str | list[str] = NullObject(),
                   IntroAnim: str | list[str] = NullObject(),
                   EnvAnim: str | list[str] = NullObject(),
                   BossAutoAttackAnim: str | list[str] = NullObject(),
                   BossAutoAttackRecoilAnim: str | list[str] = NullObject(),
                   BossAutoAttackRecoilAnim2: str | list[str] = NullObject(),
                   GadgetActiveAnim: str | list[str] = NullObject(),
                   GadgetRecoilAnim: str | list[str] = NullObject(),
                   IdleFace: str | list[str] = NullObject(),
                   WalkFace: str | list[str] = NullObject(),
                   HappyFace: str | list[str] = NullObject(),
                   HappyLoopFace: str | list[str] = NullObject(),
                   RecruitRoadOverrideFace: str | list[str] = NullObject(),
                   SadFace: str | list[str] = NullObject(),
                   SadLoopFace: str | list[str] = NullObject(),
                   LobbyFace: str | list[str] = NullObject(),
                   LobbyLoopFace: str | list[str] = NullObject(),
                   HeroScreenIdleFace: str | list[str] = NullObject(),
                   HeroScreenFace: str | list[str] = NullObject(),
                   HeroScreenLoopFace: str | list[str] = NullObject(),
                   SignatureFace: str | list[str] = NullObject(),
                   ProfileFace: str | list[str] = NullObject(),
                   IntroFace: str | list[str] = NullObject(),
                   LobbyEffect: str | list[str] = NullObject(),
                   LobbyLoopEffect: str | list[str] = NullObject(),
                   HeroScreenEffect: str | list[str] = NullObject(),
                   SignatureEffect: str | list[str] = NullObject(),
                   HappyEffect: str | list[str] = NullObject(),
                   SadEffect: str | list[str] = NullObject(),
                   PetInSameSprite: bool | list[bool] = NullObject(),
                   AttackLocksAttackAngle: bool | list[bool] = NullObject(),
                   UltiLocksAttackAngle: bool | list[bool] = NullObject(),
                   MainAttackProjectile: str | list[str] = NullObject(),
                   OverchargedMainAttackProjectile: str | list[str] = NullObject(),
                   UltiProjectile: str | list[str] = NullObject(),
                   OverchargedUltiProjectile: str | list[str] = NullObject(),
                   AlternativeSkillProjectile: str | list[str] = NullObject(),
                   UltiAlternativeSkillProjectile: str | list[str] = NullObject(),
                   MainAttackEffect: str | list[str] = NullObject(),
                   MainAttackEffect2: str | list[str] = NullObject(),
                   MainAttackEffect3: str | list[str] = NullObject(),
                   OverchargedMainAttackEffect: str | list[str] = NullObject(),
                   OverchargedMainAttackEffect2: str | list[str] = NullObject(),
                   OverchargedMainAttackEffect3: str | list[str] = NullObject(),
                   AlternatingMainAttackEffect: bool | list[bool] = NullObject(),
                   UltiAttackEffect: str | list[str] = NullObject(),
                   UltiAttackEffect2: str | list[str] = NullObject(),
                   UltiAttackEffect3: str | list[str] = NullObject(),
                   OverchargedUltiAttackEffect: str | list[str] = NullObject(),
                   OverchargedUltiAttackEffect2: str | list[str] = NullObject(),
                   OverchargedUltiAttackEffect3: str | list[str] = NullObject(),
                   ShieldEffect: str | list[str] = NullObject(),
                   UseBlueTextureInMenus: bool | list[bool] = NullObject(),
                   MainAttackUseEffect: str | list[str] = NullObject(),
                   OverchargedMainAttackUseEffect: str | list[str] = NullObject(),
                   UltiUseEffect: str | list[str] = NullObject(),
                   OverchargedUltiUseEffect: str | list[str] = NullObject(),
                   UltiEndEffect: str | list[str] = NullObject(),
                   MeleeHitEffect: str | list[str] = NullObject(),
                   OverchargedMeleeHitEffect: str | list[str] = NullObject(),
                   OverchargedUltiMeleeHitEffect: str | list[str] = NullObject(),
                   SpawnAreaEffect: str | list[str] = NullObject(),
                   SpawnEffect: str | list[str] = NullObject(),
                   SpawnShieldEffect: str | list[str] = NullObject(),
                   ReloadEffect: str | list[str] = NullObject(),
                   UltiLoopEffect: str | list[str] = NullObject(),
                   UltiLoopEffect2: str | list[str] = NullObject(),
                   OverchargedUltiLoopEffect: str | list[str] = NullObject(),
                   OverchargedUltiLoopEffect2: str | list[str] = NullObject(),
                   StarPower1Effect: str | list[str] = NullObject(),
                   OverchargedStarPower1Effect: str | list[str] = NullObject(),
                   StarPower2Effect: str | list[str] = NullObject(),
                   OverchargedStarPower2Effect: str | list[str] = NullObject(),
                   AreaEffect: str | list[str] = NullObject(),
                   AreaEffectStarPower: str | list[str] = NullObject(),
                   AreaEffectStarPowerOvercharged: str | list[str] = NullObject(),
                   AreaEffectStarPower2: str | list[str] = NullObject(),
                   AreaEffectStarPower2Overcharged: str | list[str] = NullObject(),
                   AreaEffectAttack: str | list[str] = NullObject(),
                   AreaEffectAttack2: str | list[str] = NullObject(),
                   AreaEffectUlti: str | list[str] = NullObject(),
                   AreaEffectUlti2: str | list[str] = NullObject(),
                   OverchargedAreaEffectUlti: str | list[str] = NullObject(),
                   OverchargedAreaEffectUlti2: str | list[str] = NullObject(),
                   ActivationSelfStatusEffectAttack: str | list[str] = NullObject(),
                   ActivationSelfStatusEffectUlti: str | list[str] = NullObject(),
                   StatusEffectSP1: str | list[str] = NullObject(),
                   StatusEffectSP2: str | list[str] = NullObject(),
                   PetrolEffect: str | list[str] = NullObject(),
                   SpawnedItem: str | list[str] = NullObject(),
                   SpawnedItem2: str | list[str] = NullObject(),
                   KillCelebrationSoundVO: str | list[str] = NullObject(),
                   InLeadCelebrationSoundVO: str | list[str] = NullObject(),
                   StartSoundVO: str | list[str] = NullObject(),
                   UseUltiSoundVO: str | list[str] = NullObject(),
                   TakeDamageSoundVO: str | list[str] = NullObject(),
                   DeathSoundVO: str | list[str] = NullObject(),
                   AttackSoundVO: str | list[str] = NullObject(),
                   UnlockVO: str | list[str] = NullObject(),
                   UnlockVOIndex: int | list[int] = NullObject(),
                   BoneEffect1: str | list[str] = NullObject(),
                   BoneEffectUse1: str | list[str] = NullObject(),
                   BoneEffect2: str | list[str] = NullObject(),
                   BoneEffectUse2: str | list[str] = NullObject(),
                   BoneEffect3: str | list[str] = NullObject(),
                   BoneEffectUse3: str | list[str] = NullObject(),
                   BoneEffect4: str | list[str] = NullObject(),
                   BoneEffectUse4: str | list[str] = NullObject(),
                   BoneEffect5: str | list[str] = NullObject(),
                   BoneEffectUse5: str | list[str] = NullObject(),
                   BoneEffect6: str | list[str] = NullObject(),
                   BoneEffectUse6: str | list[str] = NullObject(),
                   AutoAttackProjectile: str | list[str] = NullObject(),
                   ProjectileForShockyStarPower: str | list[str] = NullObject(),
                   OverchargedProjectileForShockyStarPower: str | list[str] = NullObject(),
                   IncendiaryStarPowerAreaEffect: str | list[str] = NullObject(),
                   KillEffect: str | list[str] = NullObject(),
                   DeathEffect: str | list[str] = NullObject(),
                   MoveEffect: str | list[str] = NullObject(),
                   MoveEffect2: str | list[str] = NullObject(),
                   ChargeMoveEffect: str | list[str] = NullObject(),
                   UltiChargeMoveEffect: str | list[str] = NullObject(),
                   OverchargedChargeMoveEffect: str | list[str] = NullObject(),
                   OverchargedUltiChargeMoveEffect: str | list[str] = NullObject(),
                   StillEffect: str | list[str] = NullObject(),
                   StillEffect2: str | list[str] = NullObject(),
                   LoopingEffect: str | list[str] = NullObject(),
                   ChargedShotEffect: str | list[str] = NullObject(),
                   DisableHeadRotation: bool | list[bool] = NullObject(),
                   BuffEffect: str | list[str] = NullObject(),
                   AttackBuildUpEffect: str | list[str] = NullObject(),
                   SpecialMaterialSetup: int | list[int] = NullObject(),
                   FaceCoversWholeTexture: bool | list[bool] = NullObject(),
                   FaceScaledUpTexture: bool | list[bool] = NullObject(),
                   TransformWhenOvercharged: bool | list[bool] = NullObject(),
                   ShadowRealmEnterEffect: str | list[str] = NullObject(),
                   ShadowRealmExitEffect: str | list[str] = NullObject(),
                   ShadowRealmFrameEffect: str | list[str] = NullObject(),
                   CustomEffect1: str | list[str] = NullObject(),
                   CustomEffect2: str | list[str] = NullObject(),
                   OverchargedCustomEffect1: str | list[str] = NullObject(),
                   OverchargedCustomEffect2: str | list[str] = NullObject(),
                   CustomAnim1: str | list[str] = NullObject(),
                   CustomAnim1Face: str | list[str] = NullObject(),
                   CustomAnim2: str | list[str] = NullObject(),
                   CustomAnim2Face: str | list[str] = NullObject(),
                   CustomAnim3: str | list[str] = NullObject(),
                   CustomAnim3Face: str | list[str] = NullObject(),
                   CustomAnim4: str | list[str] = NullObject(),
                   CustomAnim4Face: str | list[str] = NullObject(),
                   HighlightAnimSequence: str | list[str] = NullObject(),
                   SortOrder: int | list[int] = NullObject(),
                   SpawnedItemClip: str | list[str] = NullObject(),
                   SpawnedItemLoopingEffect: str | list[str] = NullObject(),
                   SpawnedItemActiveEffect: str | list[str] = NullObject(),
                   SpawnedItemStartClip: str | list[str] = NullObject(),
                   SpawnedItemReadyEffect: str | list[str] = NullObject(),
                   CustomAreaEffect1: str | list[str] = NullObject(),
                   CustomAreaEffect2: str | list[str] = NullObject(),
                   SurpriseAnim: str | list[str] = NullObject(),
                   SurpriseAnimDelay: int | list[int] = NullObject(),
                   SurpriseAnimProbability: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class MasteryRewardTypes(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disabled: bool | list[bool] = NullObject(),
                   OfferType: int | list[int] = NullObject(),
                   RequiresData: bool | list[bool] = NullObject(),
                   ForcedCount: int | list[int] = NullObject(),
                   RewardDataType: int | list[int] = NullObject(),
                   FallbackRewardCoins: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class TextsPatch(BaseObject):
    def add_object(self,
                   TID: str | list[str],
                   EN: str | list[str] = NullObject(),
                   AR: str | list[str] = NullObject(),
                   CN: str | list[str] = NullObject(),
                   CNT: str | list[str] = NullObject(),
                   DE: str | list[str] = NullObject(),
                   ES: str | list[str] = NullObject(),
                   FI: str | list[str] = NullObject(),
                   FR: str | list[str] = NullObject(),
                   HE: str | list[str] = NullObject(),
                   ID: str | list[str] = NullObject(),
                   IT: str | list[str] = NullObject(),
                   JP: str | list[str] = NullObject(),
                   KR: str | list[str] = NullObject(),
                   MS: str | list[str] = NullObject(),
                   NL: str | list[str] = NullObject(),
                   PL: str | list[str] = NullObject(),
                   PT: str | list[str] = NullObject(),
                   RU: str | list[str] = NullObject(),
                   TH: str | list[str] = NullObject(),
                   TR: str | list[str] = NullObject(),
                   VI: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class MS(BaseObject):
    def add_object(self,
                   TID: str | list[str],
                   MS: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class PL(BaseObject):
    def add_object(self,
                   TID: str | list[str],
                   PL: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Items(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   ParentItemForSkin: str | list[str] = NullObject(),
                   Disabled: bool | list[bool] = NullObject(),
                   FileName: str | list[str] = NullObject(),
                   ExportName: str | list[str] = NullObject(),
                   ExportNameEnemy: str | list[str] = NullObject(),
                   ShadowExportName: str | list[str] = NullObject(),
                   GroundGlowExportName: str | list[str] = NullObject(),
                   LoopingEffect: str | list[str] = NullObject(),
                   AlignToTiles: bool | list[bool] = NullObject(),
                   Value: int | list[int] = NullObject(),
                   Value2: int | list[int] = NullObject(),
                   Value3: int | list[int] = NullObject(),
                   Lifetime: int | list[int] = NullObject(),
                   StatusEffectAlly: str | list[str] = NullObject(),
                   StatusEffectEnemy: str | list[str] = NullObject(),
                   DisappearingTime: int | list[int] = NullObject(),
                   TriggerRangeSubTiles: int | list[int] = NullObject(),
                   TriggerAreaEffect: str | list[str] = NullObject(),
                   DestroyAreaEffect: str | list[str] = NullObject(),
                   CanBePickedUp: bool | list[bool] = NullObject(),
                   PickUpOnlyBySource: bool | list[bool] = NullObject(),
                   FollowSourceDimension: bool | list[bool] = NullObject(),
                   SpawnEffect: str | list[str] = NullObject(),
                   ActivateEffect: str | list[str] = NullObject(),
                   SCW: str | list[str] = NullObject(),
                   SCWEnemy: str | list[str] = NullObject(),
                   SCWTopLayer: str | list[str] = NullObject(),
                   UseGeneratedShadow: bool | list[bool] = NullObject(),
                   ShowAlways: bool | list[bool] = NullObject(),
                   RandomStartFrame: int | list[int] = NullObject(),
                   Layer: str | list[str] = NullObject(),
                   ItemClip: str | list[str] = NullObject(),
                   ItemReadyEffect: str | list[str] = NullObject(),
                   CustomAreaEffect1: str | list[str] = NullObject(),
                   CustomAreaEffect2: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class KR(BaseObject):
    def add_object(self,
                   TID: str | list[str],
                   KR: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class IntroFlows(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disabled: bool | list[bool] = NullObject(),
                   ContainerAssetPrefix: str | list[str] = NullObject(),
                   IdleStopFrameName: str | list[str] = NullObject(),
                   ComponentTypes: str | list[str] = NullObject(),
                   ComponentNames: str | list[str] = NullObject(),
                   ComponentTIDs: str | list[str] = NullObject(),
                   NotSetSeen: bool | list[bool] = NullObject(),
                   RequiredScAssetId: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class PlayerMapEnvironments(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disabled: bool | list[bool] = NullObject(),
                   TID: str | list[str] = NullObject(),
                   GameModeVariations: str | list[str] = NullObject(),
                   LocationThemes: str | list[str] = NullObject(),
                   MapTemplates: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class EnumeratedIdLists(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   UniqueValues: int | list[int] = NullObject(),
                   UniqueIds: str | list[str] = NullObject(),
                   StringContent: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class HE(BaseObject):
    def add_object(self,
                   TID: str | list[str],
                   HE: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class ContestTypes(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Collab: str | list[str] = NullObject(),
                   ReskinAssetId: str | list[str] = NullObject(),
                   RewardType: str | list[str] = NullObject(),
                   LocationCategoryExportName: str | list[str] = NullObject(),
                   TicketIconExportName: str | list[str] = NullObject(),
                   RewardScreenExportName: str | list[str] = NullObject(),
                   ScoreIconExportName: str | list[str] = NullObject(),
                   EventSelectionTooltipExportName: str | list[str] = NullObject(),
                   SelectableLocationCount: int | list[int] = NullObject(),
                   ContestLocationSelectionPopupExportName: str | list[str] = NullObject(),
                   WinBonusGradient: str | list[str] = NullObject(),
                   RewardShopItem: str | list[str] = NullObject(),
                   RewardClaimButtonInstanceName: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class AllianceLeagueRanks(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Rank: int | list[int] = NullObject(),
                   TID: str | list[str] = NullObject(),
                   HexColor: str | list[str] = NullObject(),
                   FrameLabel: str | list[str] = NullObject(),
                   RankIconTextField: str | list[str] = NullObject(),
                   RankIconTID: str | list[str] = NullObject(),
                   BannerFileName: str | list[str] = NullObject(),
                   BannerExportName: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Animations(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   FileName: str | list[str] = NullObject(),
                   StartFrame: int | list[int] = NullObject(),
                   EndFrame: int | list[int] = NullObject(),
                   FaceFreezeFrame: int | list[int] = NullObject(),
                   Speed: int | list[int] = NullObject(),
                   TransitionInMs: int | list[int] = NullObject(),
                   TransitionOutMs: int | list[int] = NullObject(),
                   AutoFadeMs: int | list[int] = NullObject(),
                   Looping: bool | list[bool] = NullObject(),
                   Humanoid: bool | list[bool] = NullObject(),
                   Priority: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Accessories(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Type: str | list[str] = NullObject(),
                   SubType: int | list[int] = NullObject(),
                   Cooldown: int | list[int] = NullObject(),
                   UseEffect: str | list[str] = NullObject(),
                   PetUseEffect: str | list[str] = NullObject(),
                   LoopingEffect: str | list[str] = NullObject(),
                   LoopingEffectPet: str | list[str] = NullObject(),
                   ActivationDelay: int | list[int] = NullObject(),
                   ActiveTicks: int | list[int] = NullObject(),
                   ShowCountdown: bool | list[bool] = NullObject(),
                   StopMovement: bool | list[bool] = NullObject(),
                   StopPetForDelay: bool | list[bool] = NullObject(),
                   AnimationIndex: int | list[int] = NullObject(),
                   SetAttackAngle: bool | list[bool] = NullObject(),
                   AimGuideType: int | list[int] = NullObject(),
                   ConsumesAmmo: bool | list[bool] = NullObject(),
                   StatusEffectAlly: str | list[str] = NullObject(),
                   StatusEffectEnemy: str | list[str] = NullObject(),
                   AreaEffect: str | list[str] = NullObject(),
                   PetAreaEffect: str | list[str] = NullObject(),
                   InterruptsAction: bool | list[bool] = NullObject(),
                   AllowStunActivation: bool | list[bool] = NullObject(),
                   Interruptable: bool | list[bool] = NullObject(),
                   RequirePetDistance: int | list[int] = NullObject(),
                   DestroyPet: bool | list[bool] = NullObject(),
                   Range: int | list[int] = NullObject(),
                   RequireEnemyInRange: bool | list[bool] = NullObject(),
                   TargetFriends: bool | list[bool] = NullObject(),
                   TargetIndirect: bool | list[bool] = NullObject(),
                   ShieldPercent: int | list[int] = NullObject(),
                   ShieldTicks: int | list[int] = NullObject(),
                   SpeedBoost: int | list[int] = NullObject(),
                   SpeedBoostTicks: int | list[int] = NullObject(),
                   SkipTypeCondition: bool | list[bool] = NullObject(),
                   UsableDuringCharge: int | list[int] = NullObject(),
                   UsableInShadowRealm: bool | list[bool] = NullObject(),
                   CustomObject: str | list[str] = NullObject(),
                   CustomValue1: int | list[int] = NullObject(),
                   CustomValue2: int | list[int] = NullObject(),
                   CustomValue3: int | list[int] = NullObject(),
                   CustomValue4: int | list[int] = NullObject(),
                   CustomValue5: int | list[int] = NullObject(),
                   CustomValue6: int | list[int] = NullObject(),
                   MissingTargetText: str | list[str] = NullObject(),
                   TargetTooFarText: str | list[str] = NullObject(),
                   TargetAlreadyActiveText: str | list[str] = NullObject(),
                   RequiresSpecificActionText: str | list[str] = NullObject(),
                   CustomBlockText: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Characters(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   LockedForChronos: bool | list[bool] = NullObject(),
                   Disabled: bool | list[bool] = NullObject(),
                   ItemName: str | list[str] = NullObject(),
                   WeaponSkill: str | list[str] = NullObject(),
                   UltimateSkill: str | list[str] = NullObject(),
                   OverchargedUltimateSkill: str | list[str] = NullObject(),
                   Pet: str | list[str] = NullObject(),
                   AltPet: str | list[str] = NullObject(),
                   MovementType: str | list[str] = NullObject(),
                   Speed: int | list[int] = NullObject(),
                   Hitpoints: int | list[int] = NullObject(),
                   Traits: str | list[str] = NullObject(),
                   Components: str | list[str] = NullObject(),
                   HealthPromilleLostPerSecond: int | list[int] = NullObject(),
                   HealPercentChange: int | list[int] = NullObject(),
                   LifeTimeTicks: int | list[int] = NullObject(),
                   SkipDeploy: bool | list[bool] = NullObject(),
                   MeleeAutoAttackSplashDamage: bool | list[bool] = NullObject(),
                   DelayTicksFirstAttack: int | list[int] = NullObject(),
                   AutoAttackSpeedMs: int | list[int] = NullObject(),
                   AutoAttackDamage: int | list[int] = NullObject(),
                   AutoAttackBulletsPerShot: int | list[int] = NullObject(),
                   AutoAttackMode: str | list[str] = NullObject(),
                   AutoAttackTicksBetweenBurstShots: int | list[int] = NullObject(),
                   AutoAttackProjectileSpread: int | list[int] = NullObject(),
                   AutoAttackProjectile: str | list[str] = NullObject(),
                   OverchargedAutoAttackProjectile: str | list[str] = NullObject(),
                   AutoAttackRange: int | list[int] = NullObject(),
                   RegeneratePerSecond: int | list[int] = NullObject(),
                   LowPriorityTarget: bool | list[bool] = NullObject(),
                   UltiUses: int | list[int] = NullObject(),
                   UltiChargeInitial: int | list[int] = NullObject(),
                   UltiChargeMul: int | list[int] = NullObject(),
                   UltiChargeUltiMul: int | list[int] = NullObject(),
                   OverchargeChargeMul: int | list[int] = NullObject(),
                   OverchargePassiveChargeMul: int | list[int] = NullObject(),
                   OverchargeChargeActiveMul: int | list[int] = NullObject(),
                   OverchargeDamagePercent: int | list[int] = NullObject(),
                   OverchargeSpeedPercent: int | list[int] = NullObject(),
                   OverchargeShieldPercent: int | list[int] = NullObject(),
                   Type: str | list[str] = NullObject(),
                   IsNeutral: bool | list[bool] = NullObject(),
                   CarryableType: str | list[str] = NullObject(),
                   DamagerPercentFromAliens: int | list[int] = NullObject(),
                   DefaultSkin: str | list[str] = NullObject(),
                   Mastery: str | list[str] = NullObject(),
                   ManualRotations: bool | list[bool] = NullObject(),
                   FileName: str | list[str] = NullObject(),
                   BlueExportName: str | list[str] = NullObject(),
                   RedExportName: str | list[str] = NullObject(),
                   ShadowExportName: str | list[str] = NullObject(),
                   OverchargedEffect: str | list[str] = NullObject(),
                   OverchargedUseDefaultSkin: bool | list[bool] = NullObject(),
                   StatusEffect: str | list[str] = NullObject(),
                   AreaEffect: str | list[str] = NullObject(),
                   DeathAreaEffect: str | list[str] = NullObject(),
                   DeathOverchargedAreaEffect: str | list[str] = NullObject(),
                   TakeDamageEffect: str | list[str] = NullObject(),
                   KillEffect: str | list[str] = NullObject(),
                   DeathEffect: str | list[str] = NullObject(),
                   DeathEffectOvercharged: str | list[str] = NullObject(),
                   AllowDeathEffectOverride: bool | list[bool] = NullObject(),
                   MoveEffect: str | list[str] = NullObject(),
                   ReloadEffect: str | list[str] = NullObject(),
                   OutOfAmmoEffect: str | list[str] = NullObject(),
                   DryFireEffect: str | list[str] = NullObject(),
                   SpawnEffect: str | list[str] = NullObject(),
                   OverchargedSpawnEffect: str | list[str] = NullObject(),
                   MeleeHitEffect: str | list[str] = NullObject(),
                   AutoAttackStartEffect: str | list[str] = NullObject(),
                   BoneEffect1: str | list[str] = NullObject(),
                   BoneEffectUse1: str | list[str] = NullObject(),
                   BoneEffect2: str | list[str] = NullObject(),
                   BoneEffectUse2: str | list[str] = NullObject(),
                   BoneEffect3: str | list[str] = NullObject(),
                   BoneEffectUse3: str | list[str] = NullObject(),
                   BoneEffect4: str | list[str] = NullObject(),
                   BoneEffectUse4: str | list[str] = NullObject(),
                   BoneEffect5: str | list[str] = NullObject(),
                   BoneEffectUse5: str | list[str] = NullObject(),
                   BoneEffect6: str | list[str] = NullObject(),
                   BoneEffectUse6: str | list[str] = NullObject(),
                   LoopedEffect: str | list[str] = NullObject(),
                   LoopedEffect2: str | list[str] = NullObject(),
                   KillCelebrationSoundVO: str | list[str] = NullObject(),
                   InLeadCelebrationSoundVO: str | list[str] = NullObject(),
                   StartSoundVO: str | list[str] = NullObject(),
                   UseUltiSoundVO: str | list[str] = NullObject(),
                   TakeDamageSoundVO: str | list[str] = NullObject(),
                   DeathSoundVO: str | list[str] = NullObject(),
                   AttackSoundVO: str | list[str] = NullObject(),
                   UnlockVO: str | list[str] = NullObject(),
                   UnlockVOIndex: int | list[int] = NullObject(),
                   AttackStartEffectOffset: int | list[int] = NullObject(),
                   TwoWeaponAttackEffectOffset: int | list[int] = NullObject(),
                   ShadowScaleX: int | list[int] = NullObject(),
                   ShadowScaleY: int | list[int] = NullObject(),
                   ShadowX: int | list[int] = NullObject(),
                   ShadowY: int | list[int] = NullObject(),
                   ShadowSkew: int | list[int] = NullObject(),
                   Scale: int | list[int] = NullObject(),
                   HeroScreenScale: int | list[int] = NullObject(),
                   FitToBoxScale: int | list[int] = NullObject(),
                   EndScreenScale: int | list[int] = NullObject(),
                   GatchaScreenScale: int | list[int] = NullObject(),
                   HomeScreenScale: int | list[int] = NullObject(),
                   BattleIntroScale: int | list[int] = NullObject(),
                   ShowPetInHeroScreen: bool | list[bool] = NullObject(),
                   AlwaysShowWithPet: bool | list[bool] = NullObject(),
                   HeroScreenXOffset: int | list[int] = NullObject(),
                   HeroScreenZOffset: int | list[int] = NullObject(),
                   BattleIntroXOffset: int | list[int] = NullObject(),
                   BattleIntroZOffset: int | list[int] = NullObject(),
                   HeroScreenEmoteX: int | list[int] = NullObject(),
                   HeroScreenEmoteY: int | list[int] = NullObject(),
                   CollisionRadius: int | list[int] = NullObject(),
                   HealthBar: str | list[str] = NullObject(),
                   HealthBarOffsetY: int | list[int] = NullObject(),
                   FloorIndicatorScale: int | list[int] = NullObject(),
                   HealthBarScale: int | list[int] = NullObject(),
                   FlyingHeight: int | list[int] = NullObject(),
                   ProjectileStartZ: int | list[int] = NullObject(),
                   StopMovementAfterMS: int | list[int] = NullObject(),
                   WaitMS: int | list[int] = NullObject(),
                   TID: str | list[str] = NullObject(),
                   ClassArchetype: str | list[str] = NullObject(),
                   ForceAttackAnimationToEnd: bool | list[bool] = NullObject(),
                   IconSWF: str | list[str] = NullObject(),
                   IconExportName: str | list[str] = NullObject(),
                   RecoilAmount: int | list[int] = NullObject(),
                   FootstepClip: str | list[str] = NullObject(),
                   DifferentFootstepOffset: int | list[int] = NullObject(),
                   FootstepIntervalMS: int | list[int] = NullObject(),
                   AttackingWeaponScale: int | list[int] = NullObject(),
                   UseThrowingLeftWeaponBoneScaling: bool | list[bool] = NullObject(),
                   UseThrowingRightWeaponBoneScaling: bool | list[bool] = NullObject(),
                   CommonSetUpgradeBonus: int | list[int] = NullObject(),
                   RareSetUpgradeBonus: int | list[int] = NullObject(),
                   SuperRareSetUpgradeBonus: int | list[int] = NullObject(),
                   CanWalkOverWater: bool | list[bool] = NullObject(),
                   WaterFootstepEffect: str | list[str] = NullObject(),
                   UseColorMod: bool | list[bool] = NullObject(),
                   RedAdd: int | list[int] = NullObject(),
                   GreenAdd: int | list[int] = NullObject(),
                   BlueAdd: int | list[int] = NullObject(),
                   RedMul: int | list[int] = NullObject(),
                   GreenMul: int | list[int] = NullObject(),
                   BlueMul: int | list[int] = NullObject(),
                   ChargeUltiAutomatically: int | list[int] = NullObject(),
                   ChargeUltiFromDamage: int | list[int] = NullObject(),
                   ChargeUltiFromHealing: int | list[int] = NullObject(),
                   VideoLink: str | list[str] = NullObject(),
                   ShouldEncodePetStatus: bool | list[bool] = NullObject(),
                   SecondaryPet: bool | list[bool] = NullObject(),
                   IsExternalPet: bool | list[bool] = NullObject(),
                   ExtraMinions: int | list[int] = NullObject(),
                   PetAutoSpawnDelay: int | list[int] = NullObject(),
                   PetSpawnCount: int | list[int] = NullObject(),
                   PowerLevelsType: int | list[int] = NullObject(),
                   PowerLevelsSpeedBuff: int | list[int] = NullObject(),
                   OffenseRating: int | list[int] = NullObject(),
                   DefenseRating: int | list[int] = NullObject(),
                   UtilityRating: int | list[int] = NullObject(),
                   ShowHealInBattleEnd: bool | list[bool] = NullObject(),
                   OrbitingRadius: int | list[int] = NullObject(),
                   OrbitingAngularSpeed: int | list[int] = NullObject(),
                   UniqueProperty: int | list[int] = NullObject(),
                   UniquePropertyValue1: int | list[int] = NullObject(),
                   UniquePropertyValue2: int | list[int] = NullObject(),
                   ArenaOverrideMaxHpBuff: int | list[int] = NullObject(),
                   ArenaOverrideDmgBuff: int | list[int] = NullObject(),
                   ArenaOverrideSpeedBuff: int | list[int] = NullObject(),
                   ArenaOverrideReloadBuff: int | list[int] = NullObject(),
                   PetRotatable: bool | list[bool] = NullObject(),
                   HyperMoveEffect: str | list[str] = NullObject(),
                   HumanoidSpecies: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class PlayerTitles(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   TitleTID: str | list[str] = NullObject(),
                   Gradient: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class EventModifiers(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Id: int | list[int] = NullObject(),
                   Disabled: bool | list[bool] = NullObject(),
                   NameTID: str | list[str] = NullObject(),
                   DescriptionTID: str | list[str] = NullObject(),
                   BattleLoad: int | list[int] = NullObject(),
                   BotItemPickup: str | list[str] = NullObject(),
                   IsEnabledInFriendly: bool | list[bool] = NullObject(),
                   RecordsDisabled: bool | list[bool] = NullObject(),
                   DebugMenu: bool | list[bool] = NullObject(),
                   CustomValue1: int | list[int] = NullObject(),
                   CustomValue2: int | list[int] = NullObject(),
                   CustomValue3: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class GearRarities(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   CoinPrice: int | list[int] = NullObject(),
                   TID: str | list[str] = NullObject(),
                   AvailableToAllBrawlers: bool | list[bool] = NullObject(),
                   IconFrameIndex: int | list[int] = NullObject(),
                   NotOwnedIconBgFrameIndex: int | list[int] = NullObject(),
                   TextColor: str | list[str] = NullObject(),
                   GearTitleWithRarityTID: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class BpPurchasePopup(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Season: int | list[int] = NullObject(),
                   HeroArea1: str | list[str] = NullObject(),
                   HeroArea2: str | list[str] = NullObject(),
                   HeroArea3: str | list[str] = NullObject(),
                   FrameName: str | list[str] = NullObject(),
                   Skin: str | list[str] = NullObject(),
                   SkinChroma: str | list[str] = NullObject(),
                   Pin: str | list[str] = NullObject(),
                   Icon: str | list[str] = NullObject(),
                   Spray: str | list[str] = NullObject(),
                   AnimCover: str | list[str] = NullObject(),
                   AnimSkin: str | list[str] = NullObject(),
                   AnimChromas: str | list[str] = NullObject(),
                   Jingle: str | list[str] = NullObject(),
                   Multiplier: int | list[int] = NullObject(),
                   PlusMultiplier: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class AdPlacements(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   PlacementType: int | list[int] = NullObject(),
                   Disabled: bool | list[bool] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Resources(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   TID: str | list[str] = NullObject(),
                   IconSWF: str | list[str] = NullObject(),
                   CollectEffect: str | list[str] = NullObject(),
                   IconExportName: str | list[str] = NullObject(),
                   Type: str | list[str] = NullObject(),
                   Rarity: str | list[str] = NullObject(),
                   PremiumCurrency: bool | list[bool] = NullObject(),
                   TextRed: int | list[int] = NullObject(),
                   TextGreen: int | list[int] = NullObject(),
                   TextBlue: int | list[int] = NullObject(),
                   Cap: int | list[int] = NullObject(),
                   AllowedToOverflowCapOnce: bool | list[bool] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class SeasonalSkinSections(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Mode: int | list[int] = NullObject(),
                   IncludedCampaigns: str | list[str] = NullObject(),
                   SectionTitleTID: str | list[str] = NullObject(),
                   SectionItemTID: str | list[str] = NullObject(),
                   SectionInfoTID: str | list[str] = NullObject(),
                   LastChanceSectionSeparately: bool | list[bool] = NullObject(),
                   LastChanceSectionTID: str | list[str] = NullObject(),
                   GroupCampaign: bool | list[bool] = NullObject(),
                   GroupShopItem: str | list[str] = NullObject(),
                   ShopItemCharacters: str | list[str] = NullObject(),
                   CheckDataFromOffers: bool | list[bool] = NullObject(),
                   PurchasePopupBg: str | list[str] = NullObject(),
                   EmotesBundle: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class MasteryHeroConfs(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   RewardEmotes: str | list[str] = NullObject(),
                   RewardPlayerIcons: str | list[str] = NullObject(),
                   RewardTitles: str | list[str] = NullObject(),
                   RewardSprays: str | list[str] = NullObject(),
                   MasteryIconFile: str | list[str] = NullObject(),
                   MasteryIconExportName: str | list[str] = NullObject(),
                   CustomTrack: str | list[str] = NullObject(),
                   VisualComponentTypes: str | list[str] = NullObject(),
                   VisualComponentNames: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class SkinAnimSequences(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   SequenceType: str | list[str] = NullObject(),
                   Anim: str | list[str] = NullObject(),
                   Face: str | list[str] = NullObject(),
                   Effect: str | list[str] = NullObject(),
                   LoopAnim: str | list[str] = NullObject(),
                   LoopFace: str | list[str] = NullObject(),
                   EnvironmentSkin: str | list[str] = NullObject(),
                   EnvironmentAnim: str | list[str] = NullObject(),
                   NearZ: int | list[int] = NullObject(),
                   NearZDivisor: int | list[int] = NullObject(),
                   FarZ: int | list[int] = NullObject(),
                   AnimStartSound: str | list[str] = NullObject(),
                   FadedOutMusicLevel: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class ClubPiggyTypes(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disabled: bool | list[bool] = NullObject(),
                   WinTrackType: int | list[int] = NullObject(),
                   DropType: str | list[str] = NullObject(),
                   RewardContainer: str | list[str] = NullObject(),
                   UsePerPlayerRewards: bool | list[bool] = NullObject(),
                   ClaimableMidEvent: bool | list[bool] = NullObject(),
                   SkipSummaryAfterRewards: bool | list[bool] = NullObject(),
                   NextEventTID: str | list[str] = NullObject(),
                   ReskinAssetId: str | list[str] = NullObject(),
                   CustomIntroFlow: str | list[str] = NullObject(),
                   RequireCustomIntroFlowAsset: bool | list[bool] = NullObject(),
                   EventOverTID: str | list[str] = NullObject(),
                   SmashTID: str | list[str] = NullObject(),
                   LeaderboardTabTID: str | list[str] = NullObject(),
                   ContributedWinsTID: str | list[str] = NullObject(),
                   NotContributedWinsTID: str | list[str] = NullObject(),
                   TicketTooltipTID: str | list[str] = NullObject(),
                   EventNameTID: str | list[str] = NullObject(),
                   EventEndInboxTID: str | list[str] = NullObject(),
                   EventEndNoUnclaimedRewardsInboxTID: str | list[str] = NullObject(),
                   RewardsRootClipPath: str | list[str] = NullObject(),
                   RewardClipPrefix: str | list[str] = NullObject(),
                   ClaimedRewardsRootClipPath: str | list[str] = NullObject(),
                   ClaimedRewardClipPrefix: str | list[str] = NullObject(),
                   ComponentTypes: str | list[str] = NullObject(),
                   ComponentValues: str | list[str] = NullObject(),
                   NonInteractiveItemPaths: str | list[str] = NullObject(),
                   SoundPlayerClipPaths: str | list[str] = NullObject(),
                   RemoveAllExceptOneClipWithPrefix: str | list[str] = NullObject(),
                   MaxScaleWinPips: int | list[int] = NullObject(),
                   NewTicketsTID: str | list[str] = NullObject(),
                   WinsToNextDropTID: str | list[str] = NullObject(),
                   WinsToNextDropPopupTID: str | list[str] = NullObject(),
                   WinsToNextDropGradient: str | list[str] = NullObject(),
                   LevelCounterTID: str | list[str] = NullObject(),
                   LevelCounterOverrideTIDFormat: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class GearBoosts(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Rarity: str | list[str] = NullObject(),
                   ExtraHerosAvailableTo: str | list[str] = NullObject(),
                   LogicType: int | list[int] = NullObject(),
                   ModifierValue: int | list[int] = NullObject(),
                   ModifierType: str | list[str] = NullObject(),
                   OldTokenResource: str | list[str] = NullObject(),
                   IconSWF: str | list[str] = NullObject(),
                   IconExportName: str | list[str] = NullObject(),
                   TID: str | list[str] = NullObject(),
                   InfoTID: str | list[str] = NullObject(),
                   UpgradeInfoTID: str | list[str] = NullObject(),
                   UpgradeTargetTID: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class RankedLocations(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disabled: bool | list[bool] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class ShopItems(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   OfferType: int | list[int] = NullObject(),
                   AcceptToOffers: bool | list[bool] = NullObject(),
                   AcceptToChallengeRewards: bool | list[bool] = NullObject(),
                   AcceptToChallengeFallbackRewards: bool | list[bool] = NullObject(),
                   AcceptToQuestRewards: bool | list[bool] = NullObject(),
                   AcceptToQuestFallbackRewards: bool | list[bool] = NullObject(),
                   IconFrameNumber: int | list[int] = NullObject(),
                   MaxResourcePerFrame: int | list[int] = NullObject(),
                   ShopItemAsset: str | list[str] = NullObject(),
                   ShopItemAssetBig: str | list[str] = NullObject(),
                   PopupItemAsset: str | list[str] = NullObject(),
                   PopupItemAssetHighlight: str | list[str] = NullObject(),
                   MiniOfferAsset: str | list[str] = NullObject(),
                   SeparatedSectionOfferAsset: str | list[str] = NullObject(),
                   SeparatedSectionTeaseAsset: str | list[str] = NullObject(),
                   SeasonalEventOfferAsset: str | list[str] = NullObject(),
                   LegendaryOfferAsset: str | list[str] = NullObject(),
                   ClubShopItemAsset: str | list[str] = NullObject(),
                   OfferAssetSolo: str | list[str] = NullObject(),
                   OfferAssetHalf: str | list[str] = NullObject(),
                   OfferAssetQuarter: str | list[str] = NullObject(),
                   OfferAssetHeroLayout: str | list[str] = NullObject(),
                   OfferAssetSoloHighlight: str | list[str] = NullObject(),
                   OfferAssetHalfHighlight: str | list[str] = NullObject(),
                   OfferAssetQuarterHighlight: str | list[str] = NullObject(),
                   OfferAssetHeroLayoutHighlight: str | list[str] = NullObject(),
                   SoloOfferBgFrames: Any | list[Any] = NullObject(),
                   BrawlPassAssetPaid: str | list[str] = NullObject(),
                   BrawlPassAssetFree: str | list[str] = NullObject(),
                   BrawlPassAssetPlus: str | list[str] = NullObject(),
                   MasteryTrackAsset: str | list[str] = NullObject(),
                   MasterySmallRewardAsset: str | list[str] = NullObject(),
                   TrophyRankRewardProfile: str | list[str] = NullObject(),
                   SameSizeForCollected: bool | list[bool] = NullObject(),
                   TrophyRewardMediumThreshold: int | list[int] = NullObject(),
                   TrophyRewardLargeThreshold: int | list[int] = NullObject(),
                   TrophyRankRewardTiny: str | list[str] = NullObject(),
                   TrophyRankRewardSmall: str | list[str] = NullObject(),
                   TrophyRankRewardMedium: str | list[str] = NullObject(),
                   TrophyRankRewardLarge: str | list[str] = NullObject(),
                   TrophyWorldReward: str | list[str] = NullObject(),
                   TrophyWorldIconFrameNumber: int | list[int] = NullObject(),
                   TrophyWorldMaxResourcePerFrame: int | list[int] = NullObject(),
                   ChainOfferMiniItemSmall: str | list[str] = NullObject(),
                   ChainOfferMiniItemMedium: str | list[str] = NullObject(),
                   ChainOfferMiniItemLarge: str | list[str] = NullObject(),
                   RankedRewardAsset: str | list[str] = NullObject(),
                   RankedGoalAsset: str | list[str] = NullObject(),
                   RankedGoalQuestAsset: str | list[str] = NullObject(),
                   ClubCollabAsset: str | list[str] = NullObject(),
                   RewardDescTID: str | list[str] = NullObject(),
                   ChallengeRewardFrame: str | list[str] = NullObject(),
                   ChallengeRewardAsset: str | list[str] = NullObject(),
                   RecordsPopupRewards: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class VisualOfferGroupings(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disabled: bool | list[bool] = NullObject(),
                   DefaultAssetFileName: str | list[str] = NullObject(),
                   ScreenContainerPrefix: str | list[str] = NullObject(),
                   CardPanelAsset: str | list[str] = NullObject(),
                   CardAsset: str | list[str] = NullObject(),
                   CardAssetWithoutHighlightSkin: str | list[str] = NullObject(),
                   DefaultTitleTID: str | list[str] = NullObject(),
                   DefaultSubtitleTID: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Globals(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   NumberValue: int | list[int] = NullObject(),
                   BooleanValue: bool | list[bool] = NullObject(),
                   TextValue: str | list[str] = NullObject(),
                   StringArray: str | list[str] = NullObject(),
                   NumberArray: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Sounds(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   FileNames: str | list[str] = NullObject(),
                   BackgroundFile: bool | list[bool] = NullObject(),
                   MinVolume: int | list[int] = NullObject(),
                   MaxVolume: int | list[int] = NullObject(),
                   MinPitch: int | list[int] = NullObject(),
                   MaxPitch: int | list[int] = NullObject(),
                   Priority: int | list[int] = NullObject(),
                   MaximumByType: int | list[int] = NullObject(),
                   MaxRepeatMs: int | list[int] = NullObject(),
                   Loop: bool | list[bool] = NullObject(),
                   PlayVariationsInSequence: bool | list[bool] = NullObject(),
                   PlayVariationsInSequenceManualReset: bool | list[bool] = NullObject(),
                   StartDelayMinMs: int | list[int] = NullObject(),
                   StartDelayMaxMs: int | list[int] = NullObject(),
                   PlayOnlyWhenInView: bool | list[bool] = NullObject(),
                   MaxVolumeScaleLimit: int | list[int] = NullObject(),
                   NoSoundScaleLimit: int | list[int] = NullObject(),
                   PadEmpyToEndMs: int | list[int] = NullObject(),
                   MovieClipFrameLabel: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Hints(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   TID: str | list[str] = NullObject(),
                   Disabled: bool | list[bool] = NullObject(),
                   MinXPLevel: int | list[int] = NullObject(),
                   MaxXPLevel: int | list[int] = NullObject(),
                   FileName: str | list[str] = NullObject(),
                   ExportName: str | list[str] = NullObject(),
                   Character: str | list[str] = NullObject(),
                   ReferringSCID: bool | list[bool] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class ChronosAssetIds(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disabled: bool | list[bool] = NullObject(),
                   ValidFormat: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Maps(BaseObject):
    def add_object(self,
                   Map: str | list[str],
                   Data: str | list[str] = NullObject(),
                   MetaData: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class NightMarketBundles(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disable: bool | list[bool] = NullObject(),
                   DontShowFirstTime: bool | list[bool] = NullObject(),
                   minNumberOfItems: int | list[int] = NullObject(),
                   maxNumberOfItems: int | list[int] = NullObject(),
                   maxQuota: int | list[int] = NullObject(),
                   TicketsForSkins: int | list[int] = NullObject(),
                   TicketsForCoins: int | list[int] = NullObject(),
                   TicketsForPowerPoints: int | list[int] = NullObject(),
                   TicketsForBling: int | list[int] = NullObject(),
                   TicketsForStarrdrops: int | list[int] = NullObject(),
                   TicketsForLegendaryStarrdrops: int | list[int] = NullObject(),
                   TicketsForHCStarrdrops: int | list[int] = NullObject(),
                   TicketsForToys: int | list[int] = NullObject(),
                   TicketsForIcons: int | list[int] = NullObject(),
                   TicketsForSprays: int | list[int] = NullObject(),
                   TicketsForRecruitTockens: int | list[int] = NullObject(),
                   TicketsForEmotes: int | list[int] = NullObject(),
                   TicketsForBrawlpassXP: int | list[int] = NullObject(),
                   TicketsForBrawler: int | list[int] = NullObject(),
                   TicketsForPresentBoxes: int | list[int] = NullObject(),
                   AlwaysHasSkin: bool | list[bool] = NullObject(),
                   AlwaysHasItem: bool | list[bool] = NullObject(),
                   AlwaysHasPsiIfPossible: bool | list[bool] = NullObject(),
                   AlwaysHasBrawler: bool | list[bool] = NullObject(),
                   UseSpecialSkins: bool | list[bool] = NullObject(),
                   UseSpecialBrawlers: bool | list[bool] = NullObject(),
                   ValueDiscountNumber1: int | list[int] = NullObject(),
                   TicketsForDiscountNumber1: int | list[int] = NullObject(),
                   ValueDiscountNumber2: int | list[int] = NullObject(),
                   TicketsForDiscountNumber2: int | list[int] = NullObject(),
                   ValueDiscountNumber3: int | list[int] = NullObject(),
                   TicketsForDiscountNumber3: int | list[int] = NullObject(),
                   ValueDiscountNumber4: int | list[int] = NullObject(),
                   TicketsForDiscountNumber4: int | list[int] = NullObject(),
                   ValueDiscountNumber5: int | list[int] = NullObject(),
                   TicketsForDiscountNumber5: int | list[int] = NullObject(),
                   ValueDiscountNumber6: int | list[int] = NullObject(),
                   TicketsForDiscountNumber6: int | list[int] = NullObject(),
                   ValueDiscountNumber7: int | list[int] = NullObject(),
                   TicketsForDiscountNumber7: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class ProgressionSkinDetails(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   ProgressionSkinBase: str | list[str] = NullObject(),
                   ScreenSWF: str | list[str] = NullObject(),
                   ScreenExportNamePrefix: str | list[str] = NullObject(),
                   ShowSkinDeliveryOnLevels: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Emotes(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disabled: bool | list[bool] = NullObject(),
                   DisabledCN: bool | list[bool] = NullObject(),
                   IconSWF: str | list[str] = NullObject(),
                   IconExportName: str | list[str] = NullObject(),
                   Character: str | list[str] = NullObject(),
                   Skin: str | list[str] = NullObject(),
                   GiveOnSkinUnlock: bool | list[bool] = NullObject(),
                   IsPicto: bool | list[bool] = NullObject(),
                   BattleCategory: str | list[str] = NullObject(),
                   Rarity: str | list[str] = NullObject(),
                   EmoteType: str | list[str] = NullObject(),
                   SoundEffect: str | list[str] = NullObject(),
                   SfxIndex: int | list[int] = NullObject(),
                   LockedForChronos: bool | list[bool] = NullObject(),
                   EmoteBundles: str | list[str] = NullObject(),
                   IsDefaultBattleEmote: bool | list[bool] = NullObject(),
                   PriceBling: int | list[int] = NullObject(),
                   PriceGems: int | list[int] = NullObject(),
                   DisableCatalogRelease: bool | list[bool] = NullObject(),
                   CatalogNewDaysAdjustment: int | list[int] = NullObject(),
                   NotInCatalogTID: str | list[str] = NullObject(),
                   ExtraCatalogCampaign: str | list[str] = NullObject(),
                   HideFromCatalogRarityCategory: bool | list[bool] = NullObject(),
                   UnlockedByFame: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class CharacterComponentsClient(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Type: str | list[str] = NullObject(),
                   IntValues: int | list[int] = NullObject(),
                   BoolValues: bool | list[bool] = NullObject(),
                   Effects: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class FR(BaseObject):
    def add_object(self,
                   TID: str | list[str],
                   FR: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class NameColors(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   ColorCode: str | list[str] = NullObject(),
                   Gradient: str | list[str] = NullObject(),
                   RequiredTotalTrophies: int | list[int] = NullObject(),
                   RequiredSeasonPoints: int | list[int] = NullObject(),
                   RequiredHero: str | list[str] = NullObject(),
                   SortOrder: int | list[int] = NullObject(),
                   ColorGradient: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Tiles(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   TileCode: str | list[str] = NullObject(),
                   DynamicCode: int | list[int] = NullObject(),
                   BlocksMovement: bool | list[bool] = NullObject(),
                   BlocksProjectiles: bool | list[bool] = NullObject(),
                   IsDestructible: bool | list[bool] = NullObject(),
                   IsDestructibleNormalWeapon: bool | list[bool] = NullObject(),
                   IsDestructibleOvertime: bool | list[bool] = NullObject(),
                   IsBouncer: bool | list[bool] = NullObject(),
                   IsForest: bool | list[bool] = NullObject(),
                   Damage: int | list[int] = NullObject(),
                   Health: int | list[int] = NullObject(),
                   HealthStates: int | list[int] = NullObject(),
                   HealthChangeEffect: str | list[str] = NullObject(),
                   SpeedChange: int | list[int] = NullObject(),
                   RestoreAfterDynamicOverlap: bool | list[bool] = NullObject(),
                   RespawnSeconds: int | list[int] = NullObject(),
                   CollisionMargin: int | list[int] = NullObject(),
                   BaseExportName: str | list[str] = NullObject(),
                   BaseExplosionEffect: str | list[str] = NullObject(),
                   BaseHitEffect: str | list[str] = NullObject(),
                   BaseWindEffect: str | list[str] = NullObject(),
                   SortOffset: int | list[int] = NullObject(),
                   HasHitAnim: bool | list[bool] = NullObject(),
                   HasWindAnim: bool | list[bool] = NullObject(),
                   ShadowScaleX: int | list[int] = NullObject(),
                   ShadowScaleY: int | list[int] = NullObject(),
                   ShadowX: int | list[int] = NullObject(),
                   ShadowY: int | list[int] = NullObject(),
                   ShadowSkew: int | list[int] = NullObject(),
                   Lifetime: int | list[int] = NullObject(),
                   CustomSCW: str | list[str] = NullObject(),
                   CustomMesh: str | list[str] = NullObject(),
                   CustomAngleStep: int | list[int] = NullObject(),
                   MapEditorVisible: bool | list[bool] = NullObject(),
                   MapEditorVisualMode: int | list[int] = NullObject(),
                   MapEditorConnected: bool | list[bool] = NullObject(),
                   SpawnEffect: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class FameTiers(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   FameToNext: int | list[int] = NullObject(),
                   Group: int | list[int] = NullObject(),
                   TID: str | list[str] = NullObject(),
                   IconSWF: str | list[str] = NullObject(),
                   IconExportName: str | list[str] = NullObject(),
                   IconBigExportName: str | list[str] = NullObject(),
                   IconStarsExportName: str | list[str] = NullObject(),
                   Reward: str | list[str] = NullObject(),
                   RewardType: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Effects(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Loop: bool | list[bool] = NullObject(),
                   AngleToSpawnOffset: bool | list[bool] = NullObject(),
                   FollowParent: bool | list[bool] = NullObject(),
                   FollowParentAngle: bool | list[bool] = NullObject(),
                   FollowBone: str | list[str] = NullObject(),
                   OwnScreenShake: int | list[int] = NullObject(),
                   OthersScreenShake: int | list[int] = NullObject(),
                   OwnHapticLevel: int | list[int] = NullObject(),
                   OthersHapticLevel: int | list[int] = NullObject(),
                   Time: int | list[int] = NullObject(),
                   Sound: str | list[str] = NullObject(),
                   Type: str | list[str] = NullObject(),
                   FileName: str | list[str] = NullObject(),
                   ExportName: str | list[str] = NullObject(),
                   ParticleEmitterName: str | list[str] = NullObject(),
                   Effect: str | list[str] = NullObject(),
                   Layer: str | list[str] = NullObject(),
                   GroundBasis: bool | list[bool] = NullObject(),
                   FlashColor: int | list[int] = NullObject(),
                   Scale: int | list[int] = NullObject(),
                   FlashDuration: int | list[int] = NullObject(),
                   TextInstanceName: str | list[str] = NullObject(),
                   TextParentInstanceName: str | list[str] = NullObject(),
                   EnemyVersion: str | list[str] = NullObject(),
                   ChinaReplacement: str | list[str] = NullObject(),
                   FlashWidth: int | list[int] = NullObject(),
                   EffectZ: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Traits(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Target: str | list[str] = NullObject(),
                   MetaType: int | list[int] = NullObject(),
                   ServerOnly: bool | list[bool] = NullObject(),
                   Type: str | list[str] = NullObject(),
                   Value: int | list[int] = NullObject(),
                   Projectile: str | list[str] = NullObject(),
                   AreaEffect: str | list[str] = NullObject(),
                   Character: str | list[str] = NullObject(),
                   Skill: str | list[str] = NullObject(),
                   StatusEffect: str | list[str] = NullObject(),
                   SecondProjectile: str | list[str] = NullObject(),
                   SecondAreaEffect: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class NL(BaseObject):
    def add_object(self,
                   TID: str | list[str],
                   NL: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class BillingPackages(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   TID: str | list[str] = NullObject(),
                   Type: int | list[int] = NullObject(),
                   TypeCN: int | list[int] = NullObject(),
                   Disabled: bool | list[bool] = NullObject(),
                   ExistsApple: bool | list[bool] = NullObject(),
                   ExistsAndroid: bool | list[bool] = NullObject(),
                   ExistsCN: bool | list[bool] = NullObject(),
                   DisabledCN: bool | list[bool] = NullObject(),
                   ExistsAppleCN: bool | list[bool] = NullObject(),
                   ExistsAndroidCN: bool | list[bool] = NullObject(),
                   GeoSet: int | list[int] = NullObject(),
                   Diamonds: int | list[int] = NullObject(),
                   BonusPercentage: int | list[int] = NullObject(),
                   USD: int | list[int] = NullObject(),
                   Order: int | list[int] = NullObject(),
                   RMB: int | list[int] = NullObject(),
                   TencentID: str | list[str] = NullObject(),
                   IconExportName: str | list[str] = NullObject(),
                   FrameNumber: int | list[int] = NullObject(),
                   StarterPackNumber: int | list[int] = NullObject(),
                   XpLevelReq: int | list[int] = NullObject(),
                   ValueFactor: int | list[int] = NullObject(),
                   LabelTID: str | list[str] = NullObject(),
                   LabelValue: int | list[int] = NullObject(),
                   TagLabelTID: str | list[str] = NullObject(),
                   Bg: int | list[int] = NullObject(),
                   Decor: int | list[int] = NullObject(),
                   IsPromotion: bool | list[bool] = NullObject(),
                   Coins: int | list[int] = NullObject(),
                   RefundGemValue: int | list[int] = NullObject(),
                   PricingValueEqualGems: int | list[int] = NullObject(),
                   SCIDStore: bool | list[bool] = NullObject(),
                   PremiumPass: bool | list[bool] = NullObject(),
                   PremiumPlusPass: bool | list[bool] = NullObject(),
                   BundledTierCount: int | list[int] = NullObject(),
                   DiscountOf: str | list[str] = NullObject(),
                   BundledXP: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class TrophyWorldParts(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   ScFileName: str | list[str] = NullObject(),
                   ExportName: str | list[str] = NullObject(),
                   Width: int | list[int] = NullObject(),
                   RewardsParentInstanceNamePath: str | list[str] = NullObject(),
                   IconExportPath: str | list[str] = NullObject(),
                   World: str | list[str] = NullObject(),
                   MilestoneInstanceNamePrefix: str | list[str] = NullObject(),
                   MilestoneNameStartNum: int | list[int] = NullObject(),
                   LayerInstanceNames: str | list[str] = NullObject(),
                   LayerSpeedPercentOverrides: int | list[int] = NullObject(),
                   LayerOriginPercentagesOfScreenWidth: int | list[int] = NullObject(),
                   ComponentNames: str | list[str] = NullObject(),
                   ComponentTypes: str | list[str] = NullObject(),
                   ComponentStringValues: str | list[str] = NullObject(),
                   ComponentIntValues: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class PlayerFrames(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disabled: bool | list[bool] = NullObject(),
                   IconSWF: str | list[str] = NullObject(),
                   IconExportName: str | list[str] = NullObject(),
                   IconExportNameFront: str | list[str] = NullObject(),
                   IconExportNameLevels: str | list[str] = NullObject(),
                   Banner: str | list[str] = NullObject(),
                   IconOnTop: str | list[str] = NullObject(),
                   Tier: int | list[int] = NullObject(),
                   Season: int | list[int] = NullObject(),
                   FrameType: str | list[str] = NullObject(),
                   UnlockedByFame: str | list[str] = NullObject(),
                   DelayMilliseconds: int | list[int] = NullObject(),
                   DescriptionTID: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Locales(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   IconSWF: str | list[str] = NullObject(),
                   IconExportName: str | list[str] = NullObject(),
                   LocalizedName: str | list[str] = NullObject(),
                   SortOrder: int | list[int] = NullObject(),
                   Enabled: bool | list[bool] = NullObject(),
                   EnabledCN: bool | list[bool] = NullObject(),
                   FileName: str | list[str] = NullObject(),
                   TestLanguage: bool | list[bool] = NullObject(),
                   UsedSystemFont: str | list[str] = NullObject(),
                   PreferedFallbackFont: str | list[str] = NullObject(),
                   ForcedFontFullName: str | list[str] = NullObject(),
                   HelpshiftSDKLanguage: str | list[str] = NullObject(),
                   HelpshiftSDKLanguageAndroid: str | list[str] = NullObject(),
                   TestExcludes: str | list[str] = NullObject(),
                   LoadAllLanguages: bool | list[bool] = NullObject(),
                   ChampionshipRegisterUrl: str | list[str] = NullObject(),
                   ChampionshipRegisterUrl_cn: str | list[str] = NullObject(),
                   TermsAndServiceUrl: str | list[str] = NullObject(),
                   ParentsGuideUrl: str | list[str] = NullObject(),
                   PrivacyPolicyUrl: str | list[str] = NullObject(),
                   LaserboxUrl: str | list[str] = NullObject(),
                   LaserboxUrlCN: str | list[str] = NullObject(),
                   LaserboxStagingUrl: str | list[str] = NullObject(),
                   LaserboxStagingUrlCN: str | list[str] = NullObject(),
                   LaserboxCommunityUrl: str | list[str] = NullObject(),
                   LaserboxCommunityUrlCN: str | list[str] = NullObject(),
                   LaserboxCommunityStagingUrl: str | list[str] = NullObject(),
                   LaserboxCommunityStagingUrlCN: str | list[str] = NullObject(),
                   LaserboxEsportsUrl: str | list[str] = NullObject(),
                   LaserboxEsportsUrlCN: str | list[str] = NullObject(),
                   LaserboxEsportsStagingUrl: str | list[str] = NullObject(),
                   LaserboxEsportsStagingUrlCN: str | list[str] = NullObject(),
                   LaserboxEsportsHubUrl: str | list[str] = NullObject(),
                   LaserboxEsportsHubUrlCN: str | list[str] = NullObject(),
                   LaserboxEsportsHubStagingUrl: str | list[str] = NullObject(),
                   LaserboxEsportsHubStagingUrlCN: str | list[str] = NullObject(),
                   LaserboxLangCode: str | list[str] = NullObject(),
                   FaqUrl_ios: str | list[str] = NullObject(),
                   FaqUrl_ios_cn: str | list[str] = NullObject(),
                   FaqUrl_android: str | list[str] = NullObject(),
                   FaqUrl_android_cn: str | list[str] = NullObject(),
                   ContactUsUrl_ios: str | list[str] = NullObject(),
                   ContactUsUrl_ios_cn: str | list[str] = NullObject(),
                   ContactUsUrl_android: str | list[str] = NullObject(),
                   ContactUsUrl_android_cn: str | list[str] = NullObject(),
                   SinglePageAppLaserboxEnabled: bool | list[bool] = NullObject(),
                   SinglePageAppLaserboxUrl: str | list[str] = NullObject(),
                   SinglePageAppManifestUrl: str | list[str] = NullObject(),
                   SinglePageAppLaserboxStagingUrl: str | list[str] = NullObject(),
                   SinglePageAppManifestStagingUrl: str | list[str] = NullObject(),
                   SinglePageAppCommunityLaserboxUrl: str | list[str] = NullObject(),
                   SinglePageAppCommunityManifestUrl: str | list[str] = NullObject(),
                   SinglePageAppCommunityLaserboxStagingUrl: str | list[str] = NullObject(),
                   SinglePageAppCommunityManifestStagingUrl: str | list[str] = NullObject(),
                   SinglePageAppEsportLaserboxUrl: str | list[str] = NullObject(),
                   SinglePageAppEsportManifestUrl: str | list[str] = NullObject(),
                   SinglePageAppEsportLaserboxStagingUrl: str | list[str] = NullObject(),
                   SinglePageAppEsportManifestStagingUrl: str | list[str] = NullObject(),
                   SinglePageAppLaserboxEnabledCN: bool | list[bool] = NullObject(),
                   SinglePageAppLaserboxUrlCN: str | list[str] = NullObject(),
                   SinglePageAppManifestUrlCN: str | list[str] = NullObject(),
                   SinglePageAppLaserboxStagingUrlCN: str | list[str] = NullObject(),
                   SinglePageAppManifestStagingUrlCN: str | list[str] = NullObject(),
                   FullscreenNewsUrl: str | list[str] = NullObject(),
                   FullscreenNewsStagingUrl: str | list[str] = NullObject(),
                   IsRTL: bool | list[bool] = NullObject(),
                   isNounAdj: bool | list[bool] = NullObject(),
                   SeparateThousandsWithSpaces: bool | list[bool] = NullObject(),
                   UseWhiteSpaceToReplaceLineBreak: bool | list[bool] = NullObject(),
                   UsesWhiteSpacesBetweenWords: bool | list[bool] = NullObject(),
                   SelfHelpUrl: str | list[str] = NullObject(),
                   SelfHelpUrlCN: str | list[str] = NullObject(),
                   FallbackToHelpshift: bool | list[bool] = NullObject(),
                   FallbackToHelpshiftCN: bool | list[bool] = NullObject(),
                   TermsAndServiceUrl_Tencent_android: str | list[str] = NullObject(),
                   ParentsGuideUrl_Tencent_android: str | list[str] = NullObject(),
                   PrivacyPolicyUrl_Tencent_android: str | list[str] = NullObject(),
                   OlderPrivacyPolicyUrl_Tencent_android: str | list[str] = NullObject(),
                   ThirdPartySharingUrl_Tencent_android: str | list[str] = NullObject(),
                   TermsAndServiceUrl_Tencent_ios: str | list[str] = NullObject(),
                   ParentsGuideUrl_Tencent_ios: str | list[str] = NullObject(),
                   PrivacyPolicyUrl_Tencent_ios: str | list[str] = NullObject(),
                   OlderPrivacyPolicyUrl_Tencent_ios: str | list[str] = NullObject(),
                   ThirdPartySharingUrl_Tencent_ios: str | list[str] = NullObject(),
                   TermsAndServiceUrl_Yoozoo: str | list[str] = NullObject(),
                   ParentsGuideUrl_Yoozoo: str | list[str] = NullObject(),
                   PrivacyPolicyUrl_Yoozoo: str | list[str] = NullObject(),
                   OlderPrivacyPolicyUrl_Yoozoo: str | list[str] = NullObject(),
                   ThirdPartySharingUrl_Yoozoo: str | list[str] = NullObject(),
                   DeviceMigrationSelfHelpUrl: str | list[str] = NullObject(),
                   DropRatesUrl: str | list[str] = NullObject(),
                   CollabDropRatesUrl: str | list[str] = NullObject(),
                   RankedEsportsUrl: str | list[str] = NullObject(),
                   SpellFactoryCode: str | list[str] = NullObject(),
                   CountrySpecificLegalNotice: str | list[str] = NullObject(),
                   RankedEsportsSCIDSSOUrl: str | list[str] = NullObject(),
                   ShopValueListUrl: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Bosses(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   VulnerableStateStartTicks: int | list[int] = NullObject(),
                   VulnerableStateDurationTicks: int | list[int] = NullObject(),
                   VulnerableStatusEffect: str | list[str] = NullObject(),
                   NumSkills: int | list[int] = NullObject(),
                   AttackSkills: str | list[str] = NullObject(),
                   AttackMaxCount: str | list[str] = NullObject(),
                   AttackPreDelayTicks: str | list[str] = NullObject(),
                   AttackCooldownTicks: str | list[str] = NullObject(),
                   AttackIndicatorStyles: str | list[str] = NullObject(),
                   AttackIndicatorAreaEffects: str | list[str] = NullObject(),
                   AttackIndicatorDistances: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class AllianceRoles(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Level: int | list[int] = NullObject(),
                   TID: str | list[str] = NullObject(),
                   CanInvite: bool | list[bool] = NullObject(),
                   CanSendMail: bool | list[bool] = NullObject(),
                   CanChangeAllianceSettings: bool | list[bool] = NullObject(),
                   CanAcceptJoinRequest: bool | list[bool] = NullObject(),
                   CanKick: bool | list[bool] = NullObject(),
                   CanBePromotedToLeader: bool | list[bool] = NullObject(),
                   PromoteSkill: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class CNT(BaseObject):
    def add_object(self,
                   TID: str | list[str],
                   CNT: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class ShopStyleSets(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disabled: bool | list[bool] = NullObject(),
                   StarterPackLike: bool | list[bool] = NullObject(),
                   Variant: str | list[str] = NullObject(),
                   PanelAssetOverride: str | list[str] = NullObject(),
                   OfferCardAssetOverride: str | list[str] = NullObject(),
                   PopupAssetOverride: str | list[str] = NullObject(),
                   OverrideBg: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class AllianceBadges(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   IconSWF: str | list[str] = NullObject(),
                   IconExportName: str | list[str] = NullObject(),
                   Category: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Texts(BaseObject):
    def add_object(self,
                   TID: str | list[str],
                   EN: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Sprays(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disabled: bool | list[bool] = NullObject(),
                   DisabledCN: bool | list[bool] = NullObject(),
                   FileName: str | list[str] = NullObject(),
                   ExportName: str | list[str] = NullObject(),
                   Character: str | list[str] = NullObject(),
                   Skin: str | list[str] = NullObject(),
                   GiveOnSkinUnlock: bool | list[bool] = NullObject(),
                   Rarity: str | list[str] = NullObject(),
                   EffectColorR: int | list[int] = NullObject(),
                   EffectColorG: int | list[int] = NullObject(),
                   EffectColorB: int | list[int] = NullObject(),
                   FlipSprayForEnemies: bool | list[bool] = NullObject(),
                   LockedForChronos: bool | list[bool] = NullObject(),
                   SprayBundles: str | list[str] = NullObject(),
                   IsDefaultBattleSpray: bool | list[bool] = NullObject(),
                   Texture: str | list[str] = NullObject(),
                   PriceBling: int | list[int] = NullObject(),
                   PriceGems: int | list[int] = NullObject(),
                   DisableCatalogRelease: bool | list[bool] = NullObject(),
                   CatalogNewDaysAdjustment: int | list[int] = NullObject(),
                   NotInCatalogTID: str | list[str] = NullObject(),
                   UseShineVFX: bool | list[bool] = NullObject(),
                   ExtraCatalogCampaign: str | list[str] = NullObject(),
                   HideFromCatalogMainCategory: bool | list[bool] = NullObject(),
                   DisableFromCatalogIfNotOwned: bool | list[bool] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class IT(BaseObject):
    def add_object(self,
                   TID: str | list[str],
                   IT: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class LoginCalendarItems(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   RewardTID: str | list[str] = NullObject(),
                   RewardDescTID: str | list[str] = NullObject(),
                   RewardTypes: int | list[int] = NullObject(),
                   FileName: str | list[str] = NullObject(),
                   PanelAsset: str | list[str] = NullObject(),
                   HudAsset: str | list[str] = NullObject(),
                   ChooseRewardAsset: str | list[str] = NullObject(),
                   FeaturedAsset: str | list[str] = NullObject(),
                   RewardPanelFrame: str | list[str] = NullObject(),
                   FeaturedContainerFrame: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Collabs(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   TID: str | list[str] = NullObject(),
                   CollabId: int | list[int] = NullObject(),
                   EventPanelExportName: str | list[str] = NullObject(),
                   SpecialEventPanelExportName: str | list[str] = NullObject(),
                   EventPanelMirrorExportName: str | list[str] = NullObject(),
                   EventPanelFutureExportName: str | list[str] = NullObject(),
                   SkillRewardSlotCount: int | list[int] = NullObject(),
                   GemOfferTypeForWinSlot: int | list[int] = NullObject(),
                   GemOfferExtraForWinSlot: int | list[int] = NullObject(),
                   GemOfferTypeForLossSlot: int | list[int] = NullObject(),
                   GemOfferExtraForLossSlot: int | list[int] = NullObject(),
                   UICharacter: str | list[str] = NullObject(),
                   SkinsCanDropWithoutBrawler: bool | list[bool] = NullObject(),
                   SkinsInReward: str | list[str] = NullObject(),
                   TicketsInSkinDraw: int | list[int] = NullObject(),
                   TicketsInSkinAltDraw: int | list[int] = NullObject(),
                   SpecialSkinsInReward: str | list[str] = NullObject(),
                   TicketsInSpecialSkinDraw: int | list[int] = NullObject(),
                   SpraysInReward: str | list[str] = NullObject(),
                   TicketsInSprayDraw: int | list[int] = NullObject(),
                   TicketsInSprayAltDraw: int | list[int] = NullObject(),
                   ProfilePicsInReward: str | list[str] = NullObject(),
                   TicketsInProfilePicDraw: int | list[int] = NullObject(),
                   TicketsInProfilePicAltDraw: int | list[int] = NullObject(),
                   PinsInReward: str | list[str] = NullObject(),
                   TicketsInPinDraw: int | list[int] = NullObject(),
                   TicketsInPinAltDraw: int | list[int] = NullObject(),
                   ClubCollabSkin: str | list[str] = NullObject(),
                   HideSkinRewardsInClubTrack: bool | list[bool] = NullObject(),
                   Modifier: int | list[int] = NullObject(),
                   CollabMenuVFX: str | list[str] = NullObject(),
                   CollabVFX: str | list[str] = NullObject(),
                   MutationSCW: str | list[str] = NullObject(),
                   LeaderboardTabTID: str | list[str] = NullObject(),
                   LeaderboardTitleTID: str | list[str] = NullObject(),
                   LeaderboardScoreTID: str | list[str] = NullObject(),
                   ThemeAngelic: str | list[str] = NullObject(),
                   ThemeDemonic: str | list[str] = NullObject(),
                   HasCollabShop: bool | list[bool] = NullObject(),
                   HasShopKeeper: bool | list[bool] = NullObject(),
                   BrawlersForCollabShop: str | list[str] = NullObject(),
                   TicketsInBrawlersForCollabShopDraw: int | list[int] = NullObject(),
                   ShopStylesNames: str | list[str] = NullObject(),
                   CoversIds: int | list[int] = NullObject(),
                   Discounts: int | list[int] = NullObject(),
                   BundleTitleBasedOnDiscount: str | list[str] = NullObject(),
                   FrameLabelBasedOnDiscount: str | list[str] = NullObject(),
                   RemoveAllExceptOneClipWithPrefix: str | list[str] = NullObject(),
                   ChapterNewsInboxLinkIds: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Faces(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   FileName: str | list[str] = NullObject(),
                   ExportName: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Messages(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   TID: str | list[str] = NullObject(),
                   BubbleOverrideTID: str | list[str] = NullObject(),
                   Disabled: bool | list[bool] = NullObject(),
                   MessageType: int | list[int] = NullObject(),
                   FileName: str | list[str] = NullObject(),
                   DefaultExportName: str | list[str] = NullObject(),
                   PopoverExportNameOverride: str | list[str] = NullObject(),
                   QuickEmojiType: int | list[int] = NullObject(),
                   SortPriority: int | list[int] = NullObject(),
                   AgeGated: bool | list[bool] = NullObject(),
                   AvailableInClub: bool | list[bool] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class ParticleEmitters(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   MaxParticleCount: int | list[int] = NullObject(),
                   MinLife: int | list[int] = NullObject(),
                   MaxLife: int | list[int] = NullObject(),
                   ParticleMinInterval: int | list[int] = NullObject(),
                   ParticleMaxInterval: int | list[int] = NullObject(),
                   ParticleMinLife: int | list[int] = NullObject(),
                   ParticleMaxLife: int | list[int] = NullObject(),
                   ParticleMinAngle: int | list[int] = NullObject(),
                   ParticleMaxAngle: int | list[int] = NullObject(),
                   ParticleAngleRelativeToParent: bool | list[bool] = NullObject(),
                   ParticleRandomAngle: bool | list[bool] = NullObject(),
                   ParticleMinRadius: int | list[int] = NullObject(),
                   ParticleMaxRadius: int | list[int] = NullObject(),
                   ParticleMinSpeed: int | list[int] = NullObject(),
                   ParticleMaxSpeed: int | list[int] = NullObject(),
                   ParticleStartZ: int | list[int] = NullObject(),
                   ParticleMinVelocityZ: int | list[int] = NullObject(),
                   ParticleMaxVelocityZ: int | list[int] = NullObject(),
                   ParticleGravity: int | list[int] = NullObject(),
                   ParticleMinTailLength: int | list[int] = NullObject(),
                   ParticleMaxTailLength: int | list[int] = NullObject(),
                   ParticleResource: str | list[str] = NullObject(),
                   ParticleExportName: str | list[str] = NullObject(),
                   RotateToDirection: bool | list[bool] = NullObject(),
                   LoopParticleClip: bool | list[bool] = NullObject(),
                   StartScale: int | list[int] = NullObject(),
                   EndScale: int | list[int] = NullObject(),
                   FadeOutDuration: int | list[int] = NullObject(),
                   Inertia: int | list[int] = NullObject(),
                   EnemyVersion: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class SkinAlbums(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   AlbumType: str | list[str] = NullObject(),
                   Skins: str | list[str] = NullObject(),
                   AcquireLocation: str | list[str] = NullObject(),
                   CompletionRewardSprays: str | list[str] = NullObject(),
                   CompletionRewardEmotes: str | list[str] = NullObject(),
                   Collabs: str | list[str] = NullObject(),
                   ExcludeFromCompletionCheck: bool | list[bool] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class RankedRanks(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Rank: int | list[int] = NullObject(),
                   MinELO: int | list[int] = NullObject(),
                   MaxELO: int | list[int] = NullObject(),
                   RequiredBrawlerLevel: int | list[int] = NullObject(),
                   RequiredBrawlerCount: int | list[int] = NullObject(),
                   PointsRewardAmount: int | list[int] = NullObject(),
                   RandomRewardContainer: str | list[str] = NullObject(),
                   TID: str | list[str] = NullObject(),
                   HexColor: str | list[str] = NullObject(),
                   FrameLabel: str | list[str] = NullObject(),
                   RankIconTextField: str | list[str] = NullObject(),
                   RankIconTID: str | list[str] = NullObject(),
                   CompetitiveGroup: int | list[int] = NullObject(),
                   CompetitiveIcon: str | list[str] = NullObject(),
                   CompetitiveBackground: str | list[str] = NullObject(),
                   HasFrameReward: bool | list[bool] = NullObject(),
                   Sound: str | list[str] = NullObject(),
                   ShowGlobalRank: bool | list[bool] = NullObject(),
                   FormatTooltipContext: int | list[int] = NullObject(),
                   FrameLabelTooltip: str | list[str] = NullObject(),
                   TIDTooltip: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Carryables(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   ThrowOverWalls: bool | list[bool] = NullObject(),
                   ThrowFromGroundLevel: bool | list[bool] = NullObject(),
                   MaxZ: int | list[int] = NullObject(),
                   ThrowSkill: str | list[str] = NullObject(),
                   ThrowSkillUlti: str | list[str] = NullObject(),
                   ShouldRoll: bool | list[bool] = NullObject(),
                   Bouncing: bool | list[bool] = NullObject(),
                   UseArc: bool | list[bool] = NullObject(),
                   ThrowDistanceSubTiles: int | list[int] = NullObject(),
                   ThrowDistanceUltiSubTiles: int | list[int] = NullObject(),
                   ThrowForce: int | list[int] = NullObject(),
                   StateToNormalMovementPromille: int | list[int] = NullObject(),
                   ThrowForceUlti: int | list[int] = NullObject(),
                   FlyEffect: str | list[str] = NullObject(),
                   FlyEffectUlti: str | list[str] = NullObject(),
                   MinScale: int | list[int] = NullObject(),
                   MaxScale: int | list[int] = NullObject(),
                   ZOffset: int | list[int] = NullObject(),
                   ShowTeamCircle: bool | list[bool] = NullObject(),
                   ShowTeamColor: bool | list[bool] = NullObject(),
                   AllowOwnTeamPickup: bool | list[bool] = NullObject(),
                   PreventPickupInTargetBase: bool | list[bool] = NullObject(),
                   PreventPickupFromLastTouchingTeam: bool | list[bool] = NullObject(),
                   ThrowOnTouch: bool | list[bool] = NullObject(),
                   MinHeightForGrab: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class CatalogCollections(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disabled: bool | list[bool] = NullObject(),
                   SortOrder: int | list[int] = NullObject(),
                   CollectionType: int | list[int] = NullObject(),
                   Rarities: int | list[int] = NullObject(),
                   CatalogIconExportName: str | list[str] = NullObject(),
                   NameTID: str | list[str] = NullObject(),
                   CatalogDescriptionTID: str | list[str] = NullObject(),
                   ScaleFactor: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class CompetitivePassTiers(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Type: int | list[int] = NullObject(),
                   Index: int | list[int] = NullObject(),
                   ProgressStart: int | list[int] = NullObject(),
                   Progress: int | list[int] = NullObject(),
                   Season: int | list[int] = NullObject(),
                   PrimaryRewardType: str | list[str] = NullObject(),
                   PrimaryRewardCount: int | list[int] = NullObject(),
                   PrimaryRewardExtraData: int | list[int] = NullObject(),
                   PrimaryRewardData: str | list[str] = NullObject(),
                   SecondaryRewardType: str | list[str] = NullObject(),
                   SecondaryRewardCount: int | list[int] = NullObject(),
                   SecondaryRewardExtraData: int | list[int] = NullObject(),
                   SecondaryRewardData: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class MasteryPoints(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Type: int | list[int] = NullObject(),
                   Threshold: int | list[int] = NullObject(),
                   Amount: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class RU(BaseObject):
    def add_object(self,
                   TID: str | list[str],
                   RU: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Skills(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   BehaviorType: str | list[str] = NullObject(),
                   EquipType: str | list[str] = NullObject(),
                   CanMoveAtSameTime: bool | list[bool] = NullObject(),
                   Targeted: bool | list[bool] = NullObject(),
                   AutoAttackType: int | list[int] = NullObject(),
                   AttackFacing: int | list[int] = NullObject(),
                   Cooldown: int | list[int] = NullObject(),
                   ActiveTime: int | list[int] = NullObject(),
                   CastingTime: int | list[int] = NullObject(),
                   CastingRange: int | list[int] = NullObject(),
                   RangeVisual: int | list[int] = NullObject(),
                   RangeInputScale: int | list[int] = NullObject(),
                   MaxCastingRange: int | list[int] = NullObject(),
                   AllowAimOutsideMap: bool | list[bool] = NullObject(),
                   ForceValidTile: int | list[int] = NullObject(),
                   RechargeTime: int | list[int] = NullObject(),
                   MaxCharge: int | list[int] = NullObject(),
                   Damage: int | list[int] = NullObject(),
                   PercentDamage: int | list[int] = NullObject(),
                   MsBetweenAttacks: int | list[int] = NullObject(),
                   Spread: int | list[int] = NullObject(),
                   AttackPattern: int | list[int] = NullObject(),
                   NumBulletsInOneAttack: int | list[int] = NullObject(),
                   TwoGuns: bool | list[bool] = NullObject(),
                   ExecuteFirstAttackImmediately: bool | list[bool] = NullObject(),
                   MovementSpeed: int | list[int] = NullObject(),
                   ChargePushback: int | list[int] = NullObject(),
                   OverchargedChargePushback: int | list[int] = NullObject(),
                   ChargeSpeed: int | list[int] = NullObject(),
                   ChargeType: int | list[int] = NullObject(),
                   NumSpawns: int | list[int] = NullObject(),
                   MaxSpawns: int | list[int] = NullObject(),
                   BreakInvisibilityOnAttack: bool | list[bool] = NullObject(),
                   SeeInvisibilityDistance: int | list[int] = NullObject(),
                   AlwaysCastAtMaxRange: bool | list[bool] = NullObject(),
                   MeleeAttackPiercesEnvironment: bool | list[bool] = NullObject(),
                   Projectile: str | list[str] = NullObject(),
                   OverchargedProjectile: str | list[str] = NullObject(),
                   OverchargedChainProjectile: str | list[str] = NullObject(),
                   SummonedCharacter: str | list[str] = NullObject(),
                   OverchargedSummonedCharacter: str | list[str] = NullObject(),
                   AreaEffectObject: str | list[str] = NullObject(),
                   AreaEffectObject2: str | list[str] = NullObject(),
                   AreaEffect2AtEndOfCharge: bool | list[bool] = NullObject(),
                   OverchargedAreaEffectObject: str | list[str] = NullObject(),
                   OverchargedAreaEffectObject2: str | list[str] = NullObject(),
                   AreaEffectFollowType: str | list[str] = NullObject(),
                   SpawnedItem: str | list[str] = NullObject(),
                   OverchargedSpawnedItem: str | list[str] = NullObject(),
                   SpawnItemTriggerType: int | list[int] = NullObject(),
                   ButtonSWF: str | list[str] = NullObject(),
                   ButtonExportName: str | list[str] = NullObject(),
                   ButtonExportNameBlue: str | list[str] = NullObject(),
                   AttackEffect: str | list[str] = NullObject(),
                   OverchargedAttackEffect: str | list[str] = NullObject(),
                   UseEffect: str | list[str] = NullObject(),
                   OverchargedUseEffect: str | list[str] = NullObject(),
                   EndEffect: str | list[str] = NullObject(),
                   OverchargedEndEffect: str | list[str] = NullObject(),
                   LoopEffect: str | list[str] = NullObject(),
                   LoopEffect2: str | list[str] = NullObject(),
                   OverchargedLoopEffect: str | list[str] = NullObject(),
                   OverchargedLoopEffect2: str | list[str] = NullObject(),
                   OverrideMusicWhenEquipped: str | list[str] = NullObject(),
                   ChargeMoveSound: str | list[str] = NullObject(),
                   MultiShot: bool | list[bool] = NullObject(),
                   SkillChangeType: int | list[int] = NullObject(),
                   SecondarySkill: str | list[str] = NullObject(),
                   SecondarySkill2: str | list[str] = NullObject(),
                   SecondarySkill3: str | list[str] = NullObject(),
                   SecondarySkill4: str | list[str] = NullObject(),
                   ShowTimerBar: bool | list[bool] = NullObject(),
                   ChargedShotCount: int | list[int] = NullObject(),
                   DamageModifier: int | list[int] = NullObject(),
                   HoldToShoot: bool | list[bool] = NullObject(),
                   UsableInShadowRealm: bool | list[bool] = NullObject(),
                   HealSelfOnActivationType: int | list[int] = NullObject(),
                   HealSelfOnActivationPower: int | list[int] = NullObject(),
                   LowHealthSpeedupPercent: int | list[int] = NullObject(),
                   ActivationSelfStatusEffects: str | list[str] = NullObject(),
                   ActivationSelfStatusEffectsOvercharged: str | list[str] = NullObject(),
                   OnChargeHitStatusEffect: str | list[str] = NullObject(),
                   OnChargeHitStatusEffectOvercharged: str | list[str] = NullObject(),
                   InterruptType: int | list[int] = NullObject(),
                   TID: str | list[str] = NullObject(),
                   Desc: str | list[str] = NullObject(),
                   CustomString: str | list[str] = NullObject(),
                   CustomString2: str | list[str] = NullObject(),
                   CustomValue: int | list[int] = NullObject(),
                   CustomValue2: int | list[int] = NullObject(),
                   BotUsageHint: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class AvailabilityWindow(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   FrameLabel: str | list[str] = NullObject(),
                   Skins: str | list[str] = NullObject(),
                   TID: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class GearLevels(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   GearTokens: int | list[int] = NullObject(),
                   GearScrap: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class MasteryLevels(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Level: int | list[int] = NullObject(),
                   TotalPointsThreshold: int | list[int] = NullObject(),
                   RewardCount_Common: int | list[int] = NullObject(),
                   RewardType_Common: str | list[str] = NullObject(),
                   RewardCount_Rare: int | list[int] = NullObject(),
                   RewardType_Rare: str | list[str] = NullObject(),
                   RewardCount_SuperRare: int | list[int] = NullObject(),
                   RewardType_SuperRare: str | list[str] = NullObject(),
                   RewardCount_Epic: int | list[int] = NullObject(),
                   RewardType_Epic: str | list[str] = NullObject(),
                   RewardCount_Mythic: int | list[int] = NullObject(),
                   RewardType_Mythic: str | list[str] = NullObject(),
                   RewardCount_Legendary: int | list[int] = NullObject(),
                   RewardType_Legendary: str | list[str] = NullObject(),
                   RewardCount_Chromatic: int | list[int] = NullObject(),
                   RewardType_Chromatic: str | list[str] = NullObject(),
                   RewardCount_UltraLegendary: int | list[int] = NullObject(),
                   RewardType_UltraLegendary: str | list[str] = NullObject(),
                   FrameIndex: int | list[int] = NullObject(),
                   TierTID: str | list[str] = NullObject(),
                   LevelWithTierTID: str | list[str] = NullObject(),
                   TierHexColor: str | list[str] = NullObject(),
                   TotalPointsThreshold_Custom1: int | list[int] = NullObject(),
                   RewardCount_Custom1: int | list[int] = NullObject(),
                   RewardType_Custom1: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class CN(BaseObject):
    def add_object(self,
                   TID: str | list[str],
                   CN: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class ID(BaseObject):
    def add_object(self,
                   TID: str | list[str],
                   ID: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Challenges(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disabled: bool | list[bool] = NullObject(),
                   ChallengeId: int | list[int] = NullObject(),
                   FileName: str | list[str] = NullObject(),
                   Locale: Any | list[Any] = NullObject(),
                   LogoAsset: Any | list[Any] = NullObject(),
                   HomeScreenLogo: Any | list[Any] = NullObject(),
                   EventAsset: str | list[str] = NullObject(),
                   EventAssetSmall: str | list[str] = NullObject(),
                   ChatItem: str | list[str] = NullObject(),
                   RewardItem: str | list[str] = NullObject(),
                   RewardUnlockedItem: str | list[str] = NullObject(),
                   AttemptsRewardAnimation: str | list[str] = NullObject(),
                   HeaderFrame: str | list[str] = NullObject(),
                   TID: str | list[str] = NullObject(),
                   StageTID: str | list[str] = NullObject(),
                   RewardTID: str | list[str] = NullObject(),
                   CompletedTID: str | list[str] = NullObject(),
                   MilestoneRewardPopupTID: str | list[str] = NullObject(),
                   FallbackMilestoneRewardPopupTID: str | list[str] = NullObject(),
                   CompletionRewardPopupTID: str | list[str] = NullObject(),
                   FallbackCompletionRewardPopupTID: str | list[str] = NullObject(),
                   BattleEndHeaderTID: str | list[str] = NullObject(),
                   BattleEndWinLabelTID: str | list[str] = NullObject(),
                   BattleEndWinTID: str | list[str] = NullObject(),
                   StartNotification: str | list[str] = NullObject(),
                   ReminderNotification: str | list[str] = NullObject(),
                   TeaserTitleTID: str | list[str] = NullObject(),
                   TeaserInfoTID: str | list[str] = NullObject(),
                   RewardSkin: str | list[str] = NullObject(),
                   RewardPopupTID: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class SkinCampaigns(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   NameTID: str | list[str] = NullObject(),
                   InfoTID: str | list[str] = NullObject(),
                   BgItemName: str | list[str] = NullObject(),
                   BgOfferPopup: str | list[str] = NullObject(),
                   SkinBuyRequiresExclusiveOption: bool | list[bool] = NullObject(),
                   EmoteBundleName: str | list[str] = NullObject(),
                   CampaignIconExportName: str | list[str] = NullObject(),
                   DisabledFromCatalog: bool | list[bool] = NullObject(),
                   ShowInCatalogCollectionsSection: bool | list[bool] = NullObject(),
                   CatalogSortingOrder: int | list[int] = NullObject(),
                   BundledUnderCatalogCategory: str | list[str] = NullObject(),
                   CatalogNameOverrideTID: str | list[str] = NullObject(),
                   CatalogDescriptionTID: str | list[str] = NullObject(),
                   UseSecondCampaing: bool | list[bool] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class ES(BaseObject):
    def add_object(self,
                   TID: str | list[str],
                   ES: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class DE(BaseObject):
    def add_object(self,
                   TID: str | list[str],
                   DE: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class TR(BaseObject):
    def add_object(self,
                   TID: str | list[str],
                   TR: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class HealthBars(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   FileName: str | list[str] = NullObject(),
                   PlayerExportNameTop: str | list[str] = NullObject(),
                   PlayerExportNameBot: str | list[str] = NullObject(),
                   EnemyExportNameTop: str | list[str] = NullObject(),
                   EnemyExportNameBot: str | list[str] = NullObject(),
                   YourTeamExportNameTop: str | list[str] = NullObject(),
                   YourTeamExportNameBot: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class CollabGameModes(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Collab: str | list[str] = NullObject(),
                   Contest: str | list[str] = NullObject(),
                   EventSlot: str | list[str] = NullObject(),
                   GameModeVariation: str | list[str] = NullObject(),
                   ClipOverrideSWF: str | list[str] = NullObject(),
                   ClipOverrideExportName: str | list[str] = NullObject(),
                   ModeOverrideSWF: str | list[str] = NullObject(),
                   ModeOverrideIconName: str | list[str] = NullObject(),
                   ModeOverrideRoomIconName: str | list[str] = NullObject(),
                   BannerOverrideSWF: str | list[str] = NullObject(),
                   BannerOverrideExportName: str | list[str] = NullObject(),
                   ModeBigCoverSWF: str | list[str] = NullObject(),
                   ModeBigCoverExportName: str | list[str] = NullObject(),
                   HideDefaultTextsFromBanner: bool | list[bool] = NullObject(),
                   HideDefaultTimeFromBanner: bool | list[bool] = NullObject(),
                   HideGameModeGraphicsWhileTall: bool | list[bool] = NullObject(),
                   IdleFrameLabel: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Skins(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Conf: str | list[str] = NullObject(),
                   Disabled: bool | list[bool] = NullObject(),
                   Campaigns: str | list[str] = NullObject(),
                   IconOverrideSWF: str | list[str] = NullObject(),
                   IconOverrideExportName: str | list[str] = NullObject(),
                   SkinGroupId: int | list[int] = NullObject(),
                   ObtainType: int | list[int] = NullObject(),
                   ObtainTypeCN: int | list[int] = NullObject(),
                   LastChance: bool | list[bool] = NullObject(),
                   MasterSkin: str | list[str] = NullObject(),
                   ProgressionSkinBase: str | list[str] = NullObject(),
                   ProgressionSkinLevel: int | list[int] = NullObject(),
                   ProgressionSkinFinal: bool | list[bool] = NullObject(),
                   PetSkin: str | list[str] = NullObject(),
                   PetSkin2: str | list[str] = NullObject(),
                   PriceClubCoins: int | list[int] = NullObject(),
                   PriceStarPoints: int | list[int] = NullObject(),
                   PriceBling: int | list[int] = NullObject(),
                   CanDropWithoutBlingPrice: bool | list[bool] = NullObject(),
                   PriceGems: int | list[int] = NullObject(),
                   DiscountPriceGems: int | list[int] = NullObject(),
                   PriceCoins: int | list[int] = NullObject(),
                   Rarity: str | list[str] = NullObject(),
                   TID: str | list[str] = NullObject(),
                   ShopTID: str | list[str] = NullObject(),
                   Features: str | list[str] = NullObject(),
                   CommunityCredit: str | list[str] = NullObject(),
                   MaterialsFile: str | list[str] = NullObject(),
                   DiffuseTexture: str | list[str] = NullObject(),
                   SpecularTexture: str | list[str] = NullObject(),
                   OutlineShader: str | list[str] = NullObject(),
                   PackOfferAnimOverride: str | list[str] = NullObject(),
                   BattleIntroXOffset: int | list[int] = NullObject(),
                   BattleIntroZOffset: int | list[int] = NullObject(),
                   BattleIntroVFX: bool | list[bool] = NullObject(),
                   DisableCatalogRelease: bool | list[bool] = NullObject(),
                   CatalogPreRequirementSkin: str | list[str] = NullObject(),
                   CatalogNewDaysAdjustment: int | list[int] = NullObject(),
                   NotInCatalogTID: str | list[str] = NullObject(),
                   PreciseCollision: bool | list[bool] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class JP(BaseObject):
    def add_object(self,
                   TID: str | list[str],
                   JP: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class RankedStarRewards(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   PowerLeagueSeasonId: int | list[int] = NullObject(),
                   SkinsInRankedStar: str | list[str] = NullObject(),
                   TicketsInSkinDraw: int | list[int] = NullObject(),
                   SpraysInRankedStar: str | list[str] = NullObject(),
                   TicketsInSprayDraw: int | list[int] = NullObject(),
                   ProfilePicsInRankedStar: str | list[str] = NullObject(),
                   TicketsInProfilePicDraw: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class ClassArchetypes(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   TID: str | list[str] = NullObject(),
                   FrameLabel: str | list[str] = NullObject(),
                   PluralTID: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class SkinRarities(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Price: int | list[int] = NullObject(),
                   Rarity: str | list[str] = NullObject(),
                   ChromaPrice: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class TrophySeasonRewardLevels(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   RewardContainer: str | list[str] = NullObject(),
                   DrawsInstanceName: str | list[str] = NullObject(),
                   SeasonEndScreenFrameIndex: int | list[int] = NullObject(),
                   SeasonEndScreenBoxLevel: int | list[int] = NullObject(),
                   RewardingTID: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Music(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disabled: bool | list[bool] = NullObject(),
                   FileName: str | list[str] = NullObject(),
                   BackgroundFile: bool | list[bool] = NullObject(),
                   FallBackMusic: str | list[str] = NullObject(),
                   Volume: int | list[int] = NullObject(),
                   Loop: bool | list[bool] = NullObject(),
                   PlayCount: int | list[int] = NullObject(),
                   MovieClipFrameLabel: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class AreaEffects(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   ParentAreaEffectForSkin: str | list[str] = NullObject(),
                   Disabled: bool | list[bool] = NullObject(),
                   FileName: str | list[str] = NullObject(),
                   OwnExportName: str | list[str] = NullObject(),
                   BlueExportName: str | list[str] = NullObject(),
                   RedExportName: str | list[str] = NullObject(),
                   NeutralExportName: str | list[str] = NullObject(),
                   Layer: str | list[str] = NullObject(),
                   ExportNameTop: str | list[str] = NullObject(),
                   ExportNameTopRed: str | list[str] = NullObject(),
                   ExportNameObject: str | list[str] = NullObject(),
                   Effect: str | list[str] = NullObject(),
                   LoopingEffect: str | list[str] = NullObject(),
                   ScaleLoopingEffect: int | list[int] = NullObject(),
                   AllowEffectInterrupt: bool | list[bool] = NullObject(),
                   PlaybackType: int | list[int] = NullObject(),
                   RotationType: int | list[int] = NullObject(),
                   Scale: int | list[int] = NullObject(),
                   TimeMs: int | list[int] = NullObject(),
                   Radius: int | list[int] = NullObject(),
                   Damage: int | list[int] = NullObject(),
                   DontOverrideDmg: bool | list[bool] = NullObject(),
                   DamageScaleType: int | list[int] = NullObject(),
                   CustomValue: int | list[int] = NullObject(),
                   CustomValue2: int | list[int] = NullObject(),
                   Type: str | list[str] = NullObject(),
                   StatusEffectSelf: str | list[str] = NullObject(),
                   StatusEffectAlly: str | list[str] = NullObject(),
                   StatusEffectEnemy: str | list[str] = NullObject(),
                   StatusEffectTickInterval: int | list[int] = NullObject(),
                   DelayFirstTick: bool | list[bool] = NullObject(),
                   IsPersonal: bool | list[bool] = NullObject(),
                   TargetEnemiesOnly: bool | list[bool] = NullObject(),
                   BulletExplosionBullet: str | list[str] = NullObject(),
                   BulletExplosionBulletDistance: int | list[int] = NullObject(),
                   BulletExplosionBulletOffset: int | list[int] = NullObject(),
                   BulletExplosionItem: str | list[str] = NullObject(),
                   ExpandOnDistance: int | list[int] = NullObject(),
                   BulletAngleOffset: int | list[int] = NullObject(),
                   BulletApplyAngle: bool | list[bool] = NullObject(),
                   DestroysEnvironment: bool | list[bool] = NullObject(),
                   DestroysDecorations: bool | list[bool] = NullObject(),
                   DestroysOnlyBushes: bool | list[bool] = NullObject(),
                   PushbackStrength: int | list[int] = NullObject(),
                   PushbackStrengthSelf: int | list[int] = NullObject(),
                   PushbackDeadzone: int | list[int] = NullObject(),
                   CanStopGrapple: bool | list[bool] = NullObject(),
                   StunTicks: int | list[int] = NullObject(),
                   SlowStrength: int | list[int] = NullObject(),
                   FreezeTicks: int | list[int] = NullObject(),
                   IgnoreFadeout: bool | list[bool] = NullObject(),
                   ShouldShowEvenIfOutsideScreen: bool | list[bool] = NullObject(),
                   SameAreaEffectCanNotDamageMs: int | list[int] = NullObject(),
                   RelatedImmunityAreas: str | list[str] = NullObject(),
                   DontShowToEnemy: bool | list[bool] = NullObject(),
                   RequireLineOfSight: bool | list[bool] = NullObject(),
                   ChainAreaEffect: str | list[str] = NullObject(),
                   ChainAreaEffect2: str | list[str] = NullObject(),
                   ChainAreaEffect3: str | list[str] = NullObject(),
                   OverchargedChainAreaEffect: str | list[str] = NullObject(),
                   OverchargedChainAreaEffect2: str | list[str] = NullObject(),
                   OverchargedChainAreaEffect3: str | list[str] = NullObject(),
                   SkinnedCustomValue: int | list[int] = NullObject(),
                   SpawnItem: str | list[str] = NullObject(),
                   SnapToTile: bool | list[bool] = NullObject(),
                   DamageScaleDistanceNear: int | list[int] = NullObject(),
                   DamageScaleDistanceFar: int | list[int] = NullObject(),
                   SourceType: int | list[int] = NullObject(),
                   OverHealTicks: int | list[int] = NullObject(),
                   StackOverHeal: bool | list[bool] = NullObject(),
                   MaxOverHeal: int | list[int] = NullObject(),
                   OverHealMultiplier: int | list[int] = NullObject(),
                   AffectOnlyHeroes: bool | list[bool] = NullObject(),
                   AffectProjectiles: bool | list[bool] = NullObject(),
                   IgnoreCharacters: bool | list[bool] = NullObject(),
                   InnerRadius: int | list[int] = NullObject(),
                   InnerRadiusDamagePercent: int | list[int] = NullObject(),
                   ExpireTypes: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class PricePoints(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   BillingPackages: str | list[str] = NullObject(),
                   Tiers: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class MapTemplates(BaseObject):
    def add_object(self,
                   Map: str | list[str],
                   Data: str | list[str] = NullObject(),
                   MetaData: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class EventSlots(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Slot: int | list[int] = NullObject(),
                   BgColorOverride: str | list[str] = NullObject(),
                   EventIconOverride: str | list[str] = NullObject(),
                   TrophyWorldIconExportPath: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class ClientGlobals(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   NumberValue: int | list[int] = NullObject(),
                   BooleanValue: bool | list[bool] = NullObject(),
                   TextValue: str | list[str] = NullObject(),
                   NumberArray: int | list[int] = NullObject(),
                   StringArray: str | list[str] = NullObject(),
                   AltStringArray: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Records(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disabled: bool | list[bool] = NullObject(),
                   Type: str | list[str] = NullObject(),
                   IntParam: int | list[int] = NullObject(),
                   GameplayGoal: int | list[int] = NullObject(),
                   TimesPerMatch: int | list[int] = NullObject(),
                   TicksCooldown: int | list[int] = NullObject(),
                   Tracker: str | list[str] = NullObject(),
                   TrackerIntParam: int | list[int] = NullObject(),
                   TrackerValue: int | list[int] = NullObject(),
                   RewardPoints: int | list[int] = NullObject(),
                   RewardType: str | list[str] = NullObject(),
                   Reward: str | list[str] = NullObject(),
                   FallbackCoins: int | list[int] = NullObject(),
                   TitleTID: str | list[str] = NullObject(),
                   DescriptionTID: str | list[str] = NullObject(),
                   TargetHero: str | list[str] = NullObject(),
                   TargetGameModes: str | list[str] = NullObject(),
                   PreviousTier: str | list[str] = NullObject(),
                   GameModeIcon: str | list[str] = NullObject(),
                   SortingOrder: int | list[int] = NullObject(),
                   Groupings: str | list[str] = NullObject(),
                   NoModifierOnly: bool | list[bool] = NullObject(),
                   IconAsset: str | list[str] = NullObject(),
                   IconScalePercent: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class EmoteBundles(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disabled: bool | list[bool] = NullObject(),
                   IconSWF: str | list[str] = NullObject(),
                   IconExportName: str | list[str] = NullObject(),
                   TID: str | list[str] = NullObject(),
                   CanBeBought: bool | list[bool] = NullObject(),
                   RepresentingHighlightEmote: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Projectiles(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   ParentProjectileForSkin: str | list[str] = NullObject(),
                   Disabled: bool | list[bool] = NullObject(),
                   Speed: int | list[int] = NullObject(),
                   FileName: str | list[str] = NullObject(),
                   BlueSCW: str | list[str] = NullObject(),
                   RedSCW: str | list[str] = NullObject(),
                   BlueExportName: str | list[str] = NullObject(),
                   RedExportName: str | list[str] = NullObject(),
                   ShadowExportName: str | list[str] = NullObject(),
                   BlueGroundGlowExportName: str | list[str] = NullObject(),
                   RedGroundGlowExportName: str | list[str] = NullObject(),
                   PreExplosionExportFileName: str | list[str] = NullObject(),
                   PreExplosionBlueExportName: str | list[str] = NullObject(),
                   PreExplosionRedExportName: str | list[str] = NullObject(),
                   PreExplosionTimeMs: int | list[int] = NullObject(),
                   PreExplosionScale: int | list[int] = NullObject(),
                   HitEffectEnv: str | list[str] = NullObject(),
                   HitEffectChar: str | list[str] = NullObject(),
                   MaxRangeReachedEffect: str | list[str] = NullObject(),
                   CancelEffect: str | list[str] = NullObject(),
                   Radius: int | list[int] = NullObject(),
                   IgnoreCloseWalls: bool | list[bool] = NullObject(),
                   Indirect: bool | list[bool] = NullObject(),
                   ConstantFlyTime: bool | list[bool] = NullObject(),
                   TriggerWithDelayMs: int | list[int] = NullObject(),
                   BouncePercent: int | list[int] = NullObject(),
                   Gravity: int | list[int] = NullObject(),
                   EarlyTicks: int | list[int] = NullObject(),
                   HideTime: int | list[int] = NullObject(),
                   Scale: int | list[int] = NullObject(),
                   RandomStartFrame: int | list[int] = NullObject(),
                   StatusEffectAlly: str | list[str] = NullObject(),
                   StatusEffectEnemy: str | list[str] = NullObject(),
                   SpawnAreaEffectObject: str | list[str] = NullObject(),
                   SpawnAreaEffectObject2: str | list[str] = NullObject(),
                   SpawnAreaEffectObjectsAdditional: str | list[str] = NullObject(),
                   AreaEffect2DamagePercent: int | list[int] = NullObject(),
                   SpawnCharacter: str | list[str] = NullObject(),
                   SpawnItem: str | list[str] = NullObject(),
                   SpawnAreaEffectTrail: str | list[str] = NullObject(),
                   AreaEffectTrailMinDistance: int | list[int] = NullObject(),
                   TrailEffect: str | list[str] = NullObject(),
                   SpecialTrailEffect: str | list[str] = NullObject(),
                   SpecialTrailEffect2: str | list[str] = NullObject(),
                   TrailBehaviorType: int | list[int] = NullObject(),
                   ShotByHero: bool | list[bool] = NullObject(),
                   IsBeam: bool | list[bool] = NullObject(),
                   IsBouncing: bool | list[bool] = NullObject(),
                   DistanceAddFromBounce: int | list[int] = NullObject(),
                   MaxDistanceBounces: int | list[int] = NullObject(),
                   Rendering: str | list[str] = NullObject(),
                   PiercesCharacters: bool | list[bool] = NullObject(),
                   PiercesEnvironment: bool | list[bool] = NullObject(),
                   PiercesEnvironmentLikeButter: bool | list[bool] = NullObject(),
                   PushbackStrength: int | list[int] = NullObject(),
                   PushbackType: int | list[int] = NullObject(),
                   ChainsToEnemies: int | list[int] = NullObject(),
                   ChainBullets: int | list[int] = NullObject(),
                   ChainBulletsMax: int | list[int] = NullObject(),
                   ChainSpread: int | list[int] = NullObject(),
                   ChainTravelDistance: int | list[int] = NullObject(),
                   ChainBullet: str | list[str] = NullObject(),
                   ExecuteChainSpecialCase: int | list[int] = NullObject(),
                   AnimateByDistanceTravelled: bool | list[bool] = NullObject(),
                   DamagePercentStart: int | list[int] = NullObject(),
                   DamagePercentEnd: int | list[int] = NullObject(),
                   DamageChangeStartPromille: int | list[int] = NullObject(),
                   DamageChangeEndPromille: int | list[int] = NullObject(),
                   IgnoreDamageChangeForUltiCharge: bool | list[bool] = NullObject(),
                   DamagesConstantlyTickDelay: int | list[int] = NullObject(),
                   FreezeStrength: int | list[int] = NullObject(),
                   FreezeDurationMS: int | list[int] = NullObject(),
                   StunLengthMS: int | list[int] = NullObject(),
                   PartialStunPromille: int | list[int] = NullObject(),
                   SilenceDurationMS: int | list[int] = NullObject(),
                   ScaleStart: int | list[int] = NullObject(),
                   ScaleEnd: int | list[int] = NullObject(),
                   AttractsPet: bool | list[bool] = NullObject(),
                   LifeStealPercent: int | list[int] = NullObject(),
                   PassesEnvironment: bool | list[bool] = NullObject(),
                   SuppressHealing: int | list[int] = NullObject(),
                   SuppressHealingTicks: int | list[int] = NullObject(),
                   ConsumableShield: int | list[int] = NullObject(),
                   ConsumableShieldTicks: int | list[int] = NullObject(),
                   DamageOnlyWithOneProj: bool | list[bool] = NullObject(),
                   HealOwnPercent: int | list[int] = NullObject(),
                   SpecialVisualState: bool | list[bool] = NullObject(),
                   HideFaster: bool | list[bool] = NullObject(),
                   GrapplesEnemy: bool | list[bool] = NullObject(),
                   KickBack: int | list[int] = NullObject(),
                   UseColorMod: bool | list[bool] = NullObject(),
                   RedAdd: int | list[int] = NullObject(),
                   GreenAdd: int | list[int] = NullObject(),
                   BlueAdd: int | list[int] = NullObject(),
                   RedMul: int | list[int] = NullObject(),
                   GreenMul: int | list[int] = NullObject(),
                   BlueMul: int | list[int] = NullObject(),
                   GroundBasis: bool | list[bool] = NullObject(),
                   MinDistanceForSpread: int | list[int] = NullObject(),
                   IsFriendlyHomingMissile: bool | list[bool] = NullObject(),
                   BoomerangType: int | list[int] = NullObject(),
                   CanHitAgainAfterBounce: bool | list[bool] = NullObject(),
                   IsHomingMissile: bool | list[bool] = NullObject(),
                   UltiChargeChangePercent: int | list[int] = NullObject(),
                   AppliedEffectVisualType: int | list[int] = NullObject(),
                   TravelType: int | list[int] = NullObject(),
                   TravelTypeVariable: int | list[int] = NullObject(),
                   TravelTypeVariable2: int | list[int] = NullObject(),
                   IgnoreLevelBorder: bool | list[bool] = NullObject(),
                   SteerStrength: int | list[int] = NullObject(),
                   SteerIgnoreTicks: int | list[int] = NullObject(),
                   HomeDistance: int | list[int] = NullObject(),
                   SteerLifeTime: int | list[int] = NullObject(),
                   VisualizeEndPoint: bool | list[bool] = NullObject(),
                   DoNotForceShow: bool | list[bool] = NullObject(),
                   UniqueProperty: int | list[int] = NullObject(),
                   CustomUniquePropertyValue: int | list[int] = NullObject(),
                   CustomObject: str | list[str] = NullObject(),
                   CustomObject2: str | list[str] = NullObject(),
                   Zoffset: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class AR(BaseObject):
    def add_object(self,
                   TID: str | list[str],
                   AR: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Milestones(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Type: int | list[int] = NullObject(),
                   Index: int | list[int] = NullObject(),
                   ProgressStart: int | list[int] = NullObject(),
                   Progress: int | list[int] = NullObject(),
                   League: int | list[int] = NullObject(),
                   Tier: int | list[int] = NullObject(),
                   Season: int | list[int] = NullObject(),
                   HeroPowerUnlock: int | list[int] = NullObject(),
                   PrimaryLvlUpRewardType: int | list[int] = NullObject(),
                   PrimaryLvlUpRewardCount: int | list[int] = NullObject(),
                   PrimaryLvlUpRewardExtraData: int | list[int] = NullObject(),
                   PrimaryLvlUpRewardData: str | list[str] = NullObject(),
                   SecondaryLvlUpRewardType: int | list[int] = NullObject(),
                   SecondaryLvlUpRewardCount: int | list[int] = NullObject(),
                   SecondaryLvlUpRewardExtraData: int | list[int] = NullObject(),
                   SecondaryLvlUpRewardData: str | list[str] = NullObject(),
                   DependsOnIndex: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class FI(BaseObject):
    def add_object(self,
                   TID: str | list[str],
                   FI: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class LocationThemes(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disabled: bool | list[bool] = NullObject(),
                   TileSetPrefix: str | list[str] = NullObject(),
                   BannerSWF: str | list[str] = NullObject(),
                   BannerExportName: str | list[str] = NullObject(),
                   Island: bool | list[bool] = NullObject(),
                   Music: str | list[str] = NullObject(),
                   GroundModel: str | list[str] = NullObject(),
                   EnvironmentModel: str | list[str] = NullObject(),
                   MaskedEnvironmentModel: str | list[str] = NullObject(),
                   CampaignGroundModel: str | list[str] = NullObject(),
                   Wall1Model: str | list[str] = NullObject(),
                   Wall1Submesh: str | list[str] = NullObject(),
                   Wall1AngleStep: int | list[int] = NullObject(),
                   Wall2Model: str | list[str] = NullObject(),
                   Wall2Submesh: str | list[str] = NullObject(),
                   Wall2AngleStep: int | list[int] = NullObject(),
                   CrateModel: str | list[str] = NullObject(),
                   CrateSubmesh: str | list[str] = NullObject(),
                   CrateAngleStep: int | list[int] = NullObject(),
                   BarrelModel: str | list[str] = NullObject(),
                   BarrelSubmesh: str | list[str] = NullObject(),
                   BarrelAngleStep: int | list[int] = NullObject(),
                   ThemedModel: str | list[str] = NullObject(),
                   ThemedSubmesh: str | list[str] = NullObject(),
                   ThemedAngleStep: int | list[int] = NullObject(),
                   Grass: str | list[str] = NullObject(),
                   ClutterModel: str | list[str] = NullObject(),
                   ClutterSubmesh: str | list[str] = NullObject(),
                   ClutterAngleStep: int | list[int] = NullObject(),
                   ClutterModel_CN: str | list[str] = NullObject(),
                   ClutterSubmesh_CN: str | list[str] = NullObject(),
                   ClutterAngleStep_CN: int | list[int] = NullObject(),
                   FragileModel: str | list[str] = NullObject(),
                   FragileSubmesh: str | list[str] = NullObject(),
                   FragileAngleStep: int | list[int] = NullObject(),
                   FragileModel_CN: str | list[str] = NullObject(),
                   FragileSubmesh_CN: str | list[str] = NullObject(),
                   FragileAngleStep_CN: int | list[int] = NullObject(),
                   WaterTileModel: str | list[str] = NullObject(),
                   FenceModel: str | list[str] = NullObject(),
                   RopeFenceModel: str | list[str] = NullObject(),
                   PayloadTrackModel: str | list[str] = NullObject(),
                   IndestructibleFenceModel: str | list[str] = NullObject(),
                   IndestructibleModel: str | list[str] = NullObject(),
                   IndestructibleSubmesh: str | list[str] = NullObject(),
                   Damageable1Model: str | list[str] = NullObject(),
                   Damageable1Submesh: str | list[str] = NullObject(),
                   Damageable1AngleStep: int | list[int] = NullObject(),
                   Damageable2Model: str | list[str] = NullObject(),
                   Damageable2Submesh: str | list[str] = NullObject(),
                   Damageable2AngleStep: int | list[int] = NullObject(),
                   Damageable3Model: str | list[str] = NullObject(),
                   Damageable3Submesh: str | list[str] = NullObject(),
                   Damageable3AngleStep: int | list[int] = NullObject(),
                   Damageable4Model: str | list[str] = NullObject(),
                   Damageable4Submesh: str | list[str] = NullObject(),
                   Damageable4AngleStep: int | list[int] = NullObject(),
                   IndestructibleDeco1Model: str | list[str] = NullObject(),
                   IndestructibleDeco1Submesh: str | list[str] = NullObject(),
                   IndestructibleDeco1AngleStep: int | list[int] = NullObject(),
                   IndestructibleDeco2Model: str | list[str] = NullObject(),
                   IndestructibleDeco2Submesh: str | list[str] = NullObject(),
                   IndestructibleDeco2AngleStep: int | list[int] = NullObject(),
                   IndestructibleDeco3Model: str | list[str] = NullObject(),
                   IndestructibleDeco3Submesh: str | list[str] = NullObject(),
                   IndestructibleDeco3AngleStep: int | list[int] = NullObject(),
                   IndestructibleDeco4Model: str | list[str] = NullObject(),
                   IndestructibleDeco4Submesh: str | list[str] = NullObject(),
                   IndestructibleDeco4AngleStep: int | list[int] = NullObject(),
                   GroundFillerModel: str | list[str] = NullObject(),
                   LaserBallSkinOverride: str | list[str] = NullObject(),
                   MineGemSpawnModelOverride: str | list[str] = NullObject(),
                   LootBoxSkinOverride: str | list[str] = NullObject(),
                   SafeSkinOverride: str | list[str] = NullObject(),
                   SafeCharacterOverride: str | list[str] = NullObject(),
                   ShowdownBoostModelOverride: str | list[str] = NullObject(),
                   MapPreviewBGColorRed: int | list[int] = NullObject(),
                   MapPreviewBGColorGreen: int | list[int] = NullObject(),
                   MapPreviewBGColorBlue: int | list[int] = NullObject(),
                   MapPreviewSkyColorRed: int | list[int] = NullObject(),
                   MapPreviewSkyColorGreen: int | list[int] = NullObject(),
                   MapPreviewSkyColorBlue: int | list[int] = NullObject(),
                   MapPreviewGemGrabSpawnHoleExportName: str | list[str] = NullObject(),
                   MapPreviewBallExportName: str | list[str] = NullObject(),
                   MapPreviewGoal1ExportName: str | list[str] = NullObject(),
                   MapPreviewGoal2ExportName: str | list[str] = NullObject(),
                   MapPreviewSafeExportName: str | list[str] = NullObject(),
                   MapPreviewCNOverrides: str | list[str] = NullObject(),
                   MapWidth: int | list[int] = NullObject(),
                   MapHeight: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class TrophyWorlds(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   WorldNumber: int | list[int] = NullObject(),
                   IconExportPath: str | list[str] = NullObject(),
                   TierTrophyThresholds: int | list[int] = NullObject(),
                   NameTID: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class LocalNotifications(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Priority: int | list[int] = NullObject(),
                   NotificationText: str | list[str] = NullObject(),
                   IsRegularEventRefresh: bool | list[bool] = NullObject(),
                   DontCompare: bool | list[bool] = NullObject(),
                   AutoAdd: bool | list[bool] = NullObject(),
                   TimeOffsetMins: int | list[int] = NullObject(),
                   MaxRandomTimeOffsetMins: int | list[int] = NullObject(),
                   CheckRangeMins: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class ShopPanelLayouts(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disabled: bool | list[bool] = NullObject(),
                   LayoutType: str | list[str] = NullObject(),
                   AssetFileName: str | list[str] = NullObject(),
                   PanelAsset: str | list[str] = NullObject(),
                   Asset: str | list[str] = NullObject(),
                   AssetWithoutHighlightSkin: str | list[str] = NullObject(),
                   Items: str | list[str] = NullObject(),
                   ItemPlaceholderNames: str | list[str] = NullObject(),
                   ItemContextNames: str | list[str] = NullObject(),
                   CustomTitleTID: str | list[str] = NullObject(),
                   CustomSubtitleTID: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class PlayerThumbnails(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disabled: bool | list[bool] = NullObject(),
                   DisabledCN: bool | list[bool] = NullObject(),
                   LegacyExpLevelLimit: int | list[int] = NullObject(),
                   RequiredTotalTrophies: int | list[int] = NullObject(),
                   RequiredHero: str | list[str] = NullObject(),
                   IconSWF: str | list[str] = NullObject(),
                   IconExportName: str | list[str] = NullObject(),
                   SortOrder: int | list[int] = NullObject(),
                   IsReward: bool | list[bool] = NullObject(),
                   IsAvailableForOffers: bool | list[bool] = NullObject(),
                   LockedForChronos: bool | list[bool] = NullObject(),
                   PriceBling: int | list[int] = NullObject(),
                   PriceGems: int | list[int] = NullObject(),
                   DisableCatalogRelease: bool | list[bool] = NullObject(),
                   HideInCatalogWhenNotOwned: bool | list[bool] = NullObject(),
                   CatalogNewDaysAdjustment: int | list[int] = NullObject(),
                   CatalogPreRequirementSkin: str | list[str] = NullObject(),
                   GiveOnSkinUnlock: bool | list[bool] = NullObject(),
                   NotInCatalogTID: str | list[str] = NullObject(),
                   ExtraCatalogCampaign: str | list[str] = NullObject(),
                   ExtraCatalogHero: str | list[str] = NullObject(),
                   HideFromCatalogMainCategory: bool | list[bool] = NullObject(),
                   UnlockedByFame: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class RandomRewardContainers(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   TID: str | list[str] = NullObject(),
                   TicketsInWinGamesDraw: int | list[int] = NullObject(),
                   TicketsInCollabDraw: int | list[int] = NullObject(),
                   TicketsInPresentDraw: int | list[int] = NullObject(),
                   Rarity: int | list[int] = NullObject(),
                   IsRarityOfferContainer: bool | list[bool] = NullObject(),
                   GroupType: str | list[str] = NullObject(),
                   CustomRewards: bool | list[bool] = NullObject(),
                   IsOverchargeDraw: bool | list[bool] = NullObject(),
                   IsRankedDraw: bool | list[bool] = NullObject(),
                   CollabId: int | list[int] = NullObject(),
                   MultiDropCount: int | list[int] = NullObject(),
                   PremiumDrawCountForMultiDrops: int | list[int] = NullObject(),
                   SCW: str | list[str] = NullObject(),
                   VisualType: str | list[str] = NullObject(),
                   TransitionExportName: str | list[str] = NullObject(),
                   SCFilename: str | list[str] = NullObject(),
                   TargetClip: str | list[str] = NullObject(),
                   SlashesNeeded: int | list[int] = NullObject(),
                   SlashClawEffect: str | list[str] = NullObject(),
                   SlashClawShadow: bool | list[bool] = NullObject(),
                   SlashClawCount: int | list[int] = NullObject(),
                   SoundSlash: str | list[str] = NullObject(),
                   CustomBgExportName: str | list[str] = NullObject(),
                   BackgroundFrameLabel: str | list[str] = NullObject(),
                   ChargeProgressClip: str | list[str] = NullObject(),
                   HoldChargeEffect: str | list[str] = NullObject(),
                   TouchEffectFilename: str | list[str] = NullObject(),
                   TouchEffectExportName: str | list[str] = NullObject(),
                   TapEffectClip1: str | list[str] = NullObject(),
                   TapEffectClip2: str | list[str] = NullObject(),
                   TapEffectClip3: str | list[str] = NullObject(),
                   TapEffectClipBg: str | list[str] = NullObject(),
                   FinalContainerEffectClip: str | list[str] = NullObject(),
                   FinalContainerEffectClipBg: str | list[str] = NullObject(),
                   OpeningEffectClip: str | list[str] = NullObject(),
                   OpeningEffectClipBg: str | list[str] = NullObject(),
                   RewardsLeftIcon: str | list[str] = NullObject(),
                   OpeningInstruction: str | list[str] = NullObject(),
                   Intro3DAnimStart: int | list[int] = NullObject(),
                   Intro3DAnimEnd: int | list[int] = NullObject(),
                   Idle3DAnimStart: int | list[int] = NullObject(),
                   Idle3DAnimEnd: int | list[int] = NullObject(),
                   Miss3DAnimStart: int | list[int] = NullObject(),
                   Miss3DAnimEnd: int | list[int] = NullObject(),
                   Upgrade3DAnimStart: int | list[int] = NullObject(),
                   Upgrade3DAnimEnd: int | list[int] = NullObject(),
                   Open3DAnimStart: int | list[int] = NullObject(),
                   Open3DAnimEnd: int | list[int] = NullObject(),
                   SoundAppear: str | list[str] = NullObject(),
                   SoundCharge: str | list[str] = NullObject(),
                   SoundMiss: str | list[str] = NullObject(),
                   SoundUpgrade: str | list[str] = NullObject(),
                   SoundReadyToOpen: str | list[str] = NullObject(),
                   SoundReadyToOpen2: str | list[str] = NullObject(),
                   SoundOpen: str | list[str] = NullObject(),
                   FaceFileName: str | list[str] = NullObject(),
                   FaceIdleExportName: str | list[str] = NullObject(),
                   FaceUpgradeExportName: str | list[str] = NullObject(),
                   FaceOpenExportName: str | list[str] = NullObject(),
                   SoloOfferDefaultBgFrameName: str | list[str] = NullObject(),
                   SoloOfferDefaultTitleTID: str | list[str] = NullObject(),
                   RarityFrameLabel: str | list[str] = NullObject(),
                   AnimationSCW: str | list[str] = NullObject(),
                   PiggyTap1: str | list[str] = NullObject(),
                   PiggyTap2: str | list[str] = NullObject(),
                   PiggyTap3: str | list[str] = NullObject(),
                   PiggyTap4: str | list[str] = NullObject(),
                   PiggyTapBackground1: str | list[str] = NullObject(),
                   PiggyTapBackground2: str | list[str] = NullObject(),
                   PiggyTapBackground3: str | list[str] = NullObject(),
                   PiggyTapBackground4: str | list[str] = NullObject(),
                   PiggyTapBackgroundFinal: str | list[str] = NullObject(),
                   PiggyTapBackgroundFinalBg: str | list[str] = NullObject(),
                   CustomAnimationNames: str | list[str] = NullObject(),
                   CustomAnimationStartFrames: int | list[int] = NullObject(),
                   CustomAnimationEndFrames: int | list[int] = NullObject(),
                   DescriptionExportName: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Themes(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disabled: bool | list[bool] = NullObject(),
                   FileName: str | list[str] = NullObject(),
                   ExportName: str | list[str] = NullObject(),
                   ParticleFileName: str | list[str] = NullObject(),
                   ParticleExportName: str | list[str] = NullObject(),
                   ParticleStyle: str | list[str] = NullObject(),
                   ParticleVariations: int | list[int] = NullObject(),
                   ThemeMusic: str | list[str] = NullObject(),
                   LoadingJingle: str | list[str] = NullObject(),
                   LoadingScreen: str | list[str] = NullObject(),
                   CustomButtonName: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class StatusEffects(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   ParentStatusEffectForSkin: str | list[str] = NullObject(),
                   DurationTicks: int | list[int] = NullObject(),
                   GradualWearOffAfter: int | list[int] = NullObject(),
                   CancelOnDamage: bool | list[bool] = NullObject(),
                   CancelOnCharge: bool | list[bool] = NullObject(),
                   CancelOnChargeEnd: bool | list[bool] = NullObject(),
                   CancelOnHealthRegen: bool | list[bool] = NullObject(),
                   CancelOnSourceDeath: bool | list[bool] = NullObject(),
                   TriggerRate: int | list[int] = NullObject(),
                   TriggerOnFirstTick: bool | list[bool] = NullObject(),
                   Stacking: bool | list[bool] = NullObject(),
                   Refreshable: bool | list[bool] = NullObject(),
                   PulsatingActiveTicksOn: int | list[int] = NullObject(),
                   PulsatingActiveTicksOff: int | list[int] = NullObject(),
                   Damage: int | list[int] = NullObject(),
                   DamageHealSource: int | list[int] = NullObject(),
                   UltiChargePercent: int | list[int] = NullObject(),
                   AmmoReducePercent: int | list[int] = NullObject(),
                   Healing: int | list[int] = NullObject(),
                   ShieldPercent: int | list[int] = NullObject(),
                   SpeedBoostPercent: int | list[int] = NullObject(),
                   SpeedBoostAbsolute: int | list[int] = NullObject(),
                   SpeedReducePercent: int | list[int] = NullObject(),
                   SpeedReduceAbsolute: int | list[int] = NullObject(),
                   DamageBoostPercent: int | list[int] = NullObject(),
                   DamageReducePercent: int | list[int] = NullObject(),
                   DamageBoostTargetCurrentHealthPercent: int | list[int] = NullObject(),
                   DamageReceivedBoostPercent: int | list[int] = NullObject(),
                   DamageReceivedBoostAbsolute: int | list[int] = NullObject(),
                   Cleanse: bool | list[bool] = NullObject(),
                   DoBlinkClear: bool | list[bool] = NullObject(),
                   CcImmunity: bool | list[bool] = NullObject(),
                   AttackImmunity: bool | list[bool] = NullObject(),
                   Invisibility: str | list[str] = NullObject(),
                   ForceShow: bool | list[bool] = NullObject(),
                   LosePlayerControl: bool | list[bool] = NullObject(),
                   FullStun: bool | list[bool] = NullObject(),
                   Taunt: bool | list[bool] = NullObject(),
                   Stasis: bool | list[bool] = NullObject(),
                   Silence: bool | list[bool] = NullObject(),
                   ScaleWithUpgrades: bool | list[bool] = NullObject(),
                   ScaleWithBuffs: bool | list[bool] = NullObject(),
                   IsDebuff: bool | list[bool] = NullObject(),
                   AttackPierceCharacters: bool | list[bool] = NullObject(),
                   AttackThroughWalls: bool | list[bool] = NullObject(),
                   UltiAttackThroughWalls: bool | list[bool] = NullObject(),
                   MoveThroughWalls: bool | list[bool] = NullObject(),
                   MoveThroughWater: bool | list[bool] = NullObject(),
                   ServerOnly: bool | list[bool] = NullObject(),
                   SpawnCharacterOnDeath: str | list[str] = NullObject(),
                   SpawnAreaEffectOnDeath: str | list[str] = NullObject(),
                   ChainStatusEffect: str | list[str] = NullObject(),
                   ChainStatusEffect2: str | list[str] = NullObject(),
                   PersistTransformation: bool | list[bool] = NullObject(),
                   BooleanAttributes: str | list[str] = NullObject(),
                   HapticsToSource: bool | list[bool] = NullObject(),
                   UseColorMod: bool | list[bool] = NullObject(),
                   RedAdd: int | list[int] = NullObject(),
                   GreenAdd: int | list[int] = NullObject(),
                   BlueAdd: int | list[int] = NullObject(),
                   FullScreenAdd: str | list[str] = NullObject(),
                   FullScreenMul: str | list[str] = NullObject(),
                   FullScreenEffectFile: str | list[str] = NullObject(),
                   FullScreenEffectName: str | list[str] = NullObject(),
                   StartEffect: str | list[str] = NullObject(),
                   LoopedEffect: str | list[str] = NullObject(),
                   LoopedEffectRemoveType: str | list[str] = NullObject(),
                   TimerBar: bool | list[bool] = NullObject(),
                   TriggerEffect: str | list[str] = NullObject(),
                   EndEffect: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class ColorGradients(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Colors: str | list[str] = NullObject(),
                   Speed: int | list[int] = NullObject(),
                   Scale: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class ClubPiggyLevels(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   WinTrackType: int | list[int] = NullObject(),
                   Level: int | list[int] = NullObject(),
                   State: int | list[int] = NullObject(),
                   ShownLevelInCounter: int | list[int] = NullObject(),
                   HideLevelCounterText: bool | list[bool] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Cards(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   LinkedCard: str | list[str] = NullObject(),
                   IconSWF: str | list[str] = NullObject(),
                   IconExportName: str | list[str] = NullObject(),
                   Target: str | list[str] = NullObject(),
                   TargetClassArchetype: str | list[str] = NullObject(),
                   Disabled: bool | list[bool] = NullObject(),
                   LockedForChronos: bool | list[bool] = NullObject(),
                   RequiredChromatics: int | list[int] = NullObject(),
                   MetaType: int | list[int] = NullObject(),
                   RequiresCard: str | list[str] = NullObject(),
                   Type: str | list[str] = NullObject(),
                   SubType: str | list[str] = NullObject(),
                   Skill: str | list[str] = NullObject(),
                   Value: int | list[int] = NullObject(),
                   Value2: int | list[int] = NullObject(),
                   Value3: int | list[int] = NullObject(),
                   Value4: int | list[int] = NullObject(),
                   Value5: int | list[int] = NullObject(),
                   Value6: int | list[int] = NullObject(),
                   StatusEffect: str | list[str] = NullObject(),
                   StatusEffectOvercharged: str | list[str] = NullObject(),
                   AreaEffect: str | list[str] = NullObject(),
                   Traits: str | list[str] = NullObject(),
                   Rarity: str | list[str] = NullObject(),
                   TID: str | list[str] = NullObject(),
                   PowerNumberTID: str | list[str] = NullObject(),
                   PowerNumber2TID: str | list[str] = NullObject(),
                   PowerNumber3TID: str | list[str] = NullObject(),
                   PowerNumber4TID: str | list[str] = NullObject(),
                   PowerIcon1ExportName: str | list[str] = NullObject(),
                   PowerIcon2ExportName: str | list[str] = NullObject(),
                   SortOrder: int | list[int] = NullObject(),
                   DontUpgradeStat: bool | list[bool] = NullObject(),
                   HideDamageStat: bool | list[bool] = NullObject(),
                   DirectPurchasePrice: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Credits(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   String: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class AllianceLeagueModes(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   EventSlot: int | list[int] = NullObject(),
                   ModeOverrideIconName: str | list[str] = NullObject(),
                   ModeOverrideRoomIconName: str | list[str] = NullObject(),
                   BannerOverrideSWF: str | list[str] = NullObject(),
                   BannerOverrideExportName: str | list[str] = NullObject(),
                   EventTeaseBgColorOverride: str | list[str] = NullObject(),
                   PreviewTickets: int | list[int] = NullObject(),
                   PreviewMaxWin: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class ClubPiggyWins(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   WinTrackType: int | list[int] = NullObject(),
                   CumulativeWins: int | list[int] = NullObject(),
                   MainMilestone: bool | list[bool] = NullObject(),
                   Level: int | list[int] = NullObject(),
                   CumulativeRewardStarDrops: int | list[int] = NullObject(),
                   CumulativeRewardCoins: int | list[int] = NullObject(),
                   CumulativeRewardPowerPoints: int | list[int] = NullObject(),
                   CumulativeRewardBling: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Tutorial(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disabled: bool | list[bool] = NullObject(),
                   StartDelayMS: int | list[int] = NullObject(),
                   EndDelayMS: int | list[int] = NullObject(),
                   ForceSpeechBubbleCloseMS: int | list[int] = NullObject(),
                   StartCondition: str | list[str] = NullObject(),
                   StartLocationX: int | list[int] = NullObject(),
                   StartLocationY: int | list[int] = NullObject(),
                   StartLocationRadius: int | list[int] = NullObject(),
                   AnimationX: int | list[int] = NullObject(),
                   AnimationY: int | list[int] = NullObject(),
                   AnimationX2: int | list[int] = NullObject(),
                   AnimationY2: int | list[int] = NullObject(),
                   CompleteCondition: str | list[str] = NullObject(),
                   ShouldUseAutoShoot: bool | list[bool] = NullObject(),
                   CompleteLocationX: int | list[int] = NullObject(),
                   CompleteLocationY: int | list[int] = NullObject(),
                   CompleteLocationRadius: int | list[int] = NullObject(),
                   UseUltiX: int | list[int] = NullObject(),
                   UseUltiY: int | list[int] = NullObject(),
                   AnimationClipSWF: str | list[str] = NullObject(),
                   AnimationMovieClip: str | list[str] = NullObject(),
                   AnimationClipSWF2: str | list[str] = NullObject(),
                   AnimationMovieClip2: str | list[str] = NullObject(),
                   SpeechBubbleCharacterSWF: str | list[str] = NullObject(),
                   SpeechBubbleCharacterMovieClip: str | list[str] = NullObject(),
                   SpeechBubbleTIDs: str | list[str] = NullObject(),
                   StartSound: str | list[str] = NullObject(),
                   SpawnCharacter: str | list[str] = NullObject(),
                   SpawnLocationX: int | list[int] = NullObject(),
                   SpawnLocationY: int | list[int] = NullObject(),
                   CustomData: int | list[int] = NullObject(),
                   BlockingSpeechBubble: bool | list[bool] = NullObject(),
                   ShowUlti: bool | list[bool] = NullObject(),
                   ShowShootStick: bool | list[bool] = NullObject(),
                   LeftSpeechBubble: bool | list[bool] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class RecordLevels(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   CumulativeRecordScore: int | list[int] = NullObject(),
                   Level: int | list[int] = NullObject(),
                   EmblemSwf: str | list[str] = NullObject(),
                   EmblemExportName: str | list[str] = NullObject(),
                   RewardType: str | list[str] = NullObject(),
                   Reward: str | list[str] = NullObject(),
                   DontShow: bool | list[bool] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class NightMarketItems(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Rarity: str | list[str] = NullObject(),
                   TypeName: str | list[str] = NullObject(),
                   Amount: int | list[int] = NullObject(),
                   ValueInCash: int | list[int] = NullObject(),
                   BundleQuota: int | list[int] = NullObject(),
                   TicketsForBundle1: int | list[int] = NullObject(),
                   TicketsForBundle2: int | list[int] = NullObject(),
                   TicketsForBundle3: int | list[int] = NullObject(),
                   TicketsForBundle4: int | list[int] = NullObject(),
                   TicketsForBundle5: int | list[int] = NullObject(),
                   TicketsForBundle6: int | list[int] = NullObject(),
                   TicketsForBundle7: int | list[int] = NullObject(),
                   TicketsForBundle8: int | list[int] = NullObject(),
                   TicketsForBundle9: int | list[int] = NullObject(),
                   TicketsForBundle10: int | list[int] = NullObject(),
                   TicketsForBundle11: int | list[int] = NullObject(),
                   TicketsForBundle12: int | list[int] = NullObject(),
                   TicketsForBundle13: int | list[int] = NullObject(),
                   TicketsForBundle14: int | list[int] = NullObject(),
                   TicketsForBundle15: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class LocationFeatures(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Mode: str | list[str] = NullObject(),
                   LocationTheme: str | list[str] = NullObject(),
                   MeshNames: str | list[str] = NullObject(),
                   Character: str | list[str] = NullObject(),
                   FrameDelay: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class StringReplacement(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Needle: str | list[str] = NullObject(),
                   Replacement: str | list[str] = NullObject(),
                   MatchType: str | list[str] = NullObject(),
                   Usage: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class PT(BaseObject):
    def add_object(self,
                   TID: str | list[str],
                   PT: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class TH(BaseObject):
    def add_object(self,
                   TID: str | list[str],
                   TH: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class RandomRewards(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   TicketsInRareStar: int | list[int] = NullObject(),
                   TicketsInSuperRareStar: int | list[int] = NullObject(),
                   TicketsInEpicStar: int | list[int] = NullObject(),
                   TicketsInMythicStar: int | list[int] = NullObject(),
                   TicketsInLegendaryStar: int | list[int] = NullObject(),
                   TicketsInOverchargeStar: int | list[int] = NullObject(),
                   TicketsInRankedStar: int | list[int] = NullObject(),
                   TicketsInRareCollabDrop: int | list[int] = NullObject(),
                   TicketsInSuperRareCollabDrop: int | list[int] = NullObject(),
                   TicketsInEpicCollabDrop: int | list[int] = NullObject(),
                   TicketsInMythicCollabDrop: int | list[int] = NullObject(),
                   TicketsInLegendaryCollabDrop: int | list[int] = NullObject(),
                   TicketsInMegaBox: int | list[int] = NullObject(),
                   TicketsInAngelicStar: int | list[int] = NullObject(),
                   TicketsInDemonicStar: int | list[int] = NullObject(),
                   TicketsInSeasonBoxLevel1: int | list[int] = NullObject(),
                   TicketsInSeasonBoxLevel2: int | list[int] = NullObject(),
                   TicketsInSeasonBoxLevel3: int | list[int] = NullObject(),
                   TicketsInSeasonBoxLevel4: int | list[int] = NullObject(),
                   TicketsInSeasonBoxLevel5: int | list[int] = NullObject(),
                   TicketsInRarePresentDrop: int | list[int] = NullObject(),
                   TicketsInSuperRarePresentDrop: int | list[int] = NullObject(),
                   TicketsInEpicPresentDrop: int | list[int] = NullObject(),
                   TicketsInMythicPresentDrop: int | list[int] = NullObject(),
                   TicketsInLegendaryPresentDrop: int | list[int] = NullObject(),
                   TicketsInSplitterRare: int | list[int] = NullObject(),
                   TicketsInSplitterSuperRare: int | list[int] = NullObject(),
                   TicketsInSplitterEpic: int | list[int] = NullObject(),
                   TicketsInSplitterMythic: int | list[int] = NullObject(),
                   TypeName: str | list[str] = NullObject(),
                   TypeValue: int | list[int] = NullObject(),
                   InPremiumDraw: bool | list[bool] = NullObject(),
                   TypePriceMin: int | list[int] = NullObject(),
                   TypePriceMax: int | list[int] = NullObject(),
                   AmountMin: int | list[int] = NullObject(),
                   AmountMax: int | list[int] = NullObject(),
                   FallbackTypeName: str | list[str] = NullObject(),
                   FallbackAmount: int | list[int] = NullObject(),
                   NoEventFallbackTypeName: str | list[str] = NullObject(),
                   NoEventFallbackAmount: int | list[int] = NullObject(),
                   TierForVisualization: int | list[int] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Regions(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   TID: str | list[str] = NullObject(),
                   DisplayName: str | list[str] = NullObject(),
                   IsCountry: bool | list[bool] = NullObject(),
                   AgeLimitOverride: int | list[int] = NullObject(),
                   ForceScidLoginForNewPlayers: bool | list[bool] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class TrophyWorldMilestones(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Index: int | list[int] = NullObject(),
                   TrophyCount: int | list[int] = NullObject(),
                   RewardType: str | list[str] = NullObject(),
                   RewardCount: int | list[int] = NullObject(),
                   RewardExtraData: int | list[int] = NullObject(),
                   RewardData: str | list[str] = NullObject(),
                   FallbackRewardType: str | list[str] = NullObject(),
                   FallbackRewardCount: int | list[int] = NullObject(),
                   FallbackRewardExtraData: int | list[int] = NullObject(),
                   FallbackRewardData: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)


class Locations(BaseObject):
    def add_object(self,
                   Name: str | list[str],
                   Disabled: bool | list[bool] = NullObject(),
                   TID: str | list[str] = NullObject(),
                   LocationTheme: str | list[str] = NullObject(),
                   SupportingCampaignGround: bool | list[bool] = NullObject(),
                   BannerOverrideSWF: str | list[str] = NullObject(),
                   BannerOverrideExportName: str | list[str] = NullObject(),
                   GameModeVariation: str | list[str] = NullObject(),
                   Map: str | list[str] = NullObject(),
                   CommunityCredit: str | list[str] = NullObject(),
                   TrainingGroundsEnabled: bool | list[bool] = NullObject(),
                   RecommendedBrawler0: str | list[str] = NullObject(),
                   RecommendedBrawler1: str | list[str] = NullObject(),
                   RecommendedBrawler2: str | list[str] = NullObject(),
                   RecommendedBrawler3: str | list[str] = NullObject(),
                   RecommendedBrawler4: str | list[str] = NullObject(),
                   RecommendedBrawler5: str | list[str] = NullObject(),
                   RecommendedBrawler6: str | list[str] = NullObject(),
                   RecommendedBrawler7: str | list[str] = NullObject(),
                   RecommendedBrawler8: str | list[str] = NullObject(),
                   RecommendedBrawler9: str | list[str] = NullObject()
                   ):
        data = locals()
        data.pop('self')
        super().add_object(**data)

