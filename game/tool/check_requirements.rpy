define show_bra = 5
define show_panties = 7
define show_public_hair = 15
define show_tits = 20
define touches_tits_gluteus = 70
define handjob = 85
define squeeze_tits_gluteus = 90
define titsjob = 130
define oraljob = 180
define show_pussy = 200
define rub_pussy = 250
define finger_pussy = 350
define ass_job = 500
define sex_vaginal = 700
define finger_ass = 800
define sex_anal = 850
define group = 950
init python:
    # CheckSex: check if MC has the requirements to unlock that scene
    class CheckSex():
        def CheckLustSex(self, req_lust, partner_stats, partner_tendencies, sexual_goals, difficulty_percent):
            facility_percent = 0
            if (sexual_goals > 50):
                facility_percent += 5
            if (partner_stats.love > 50):
                facility_percent += 1
            elif (partner_stats.love > 75):
                facility_percent += 2
            elif (partner_stats.love > 90):
                facility_percent += 3
            return (partner_stats.lust >= req_lust/difficulty_percent*100 - facility)
        def CheckSubmissionSex(self, req_submission, partner_stats, partner_tendencies, sexual_goals, difficulty_percent):
            facility_percent = 0
            if (sexual_goals > 50):
                facility_percent += 5
            if (partner_stats.corruption > 50):
                facility_percent += 1
            elif (partner_stats.corruption > 75):
                facility_percent += 2
            elif (partner_stats.corruption > 90):
                facility_percent += 3
            return (partner_stats.submission >= req_submission/difficulty_percent*100 - facility)
        def show_bra(self, partner_stats, partner_tendencies, sexual_goals, is_love_scene):
            val = show_bra
            if (is_love_scene):
                return CheckLustSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
            else:
                return CheckSubmissionSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
        def show_panties(self, partner_stats, partner_tendencies, sexual_goals, is_love_scene):
            val = show_panties
            if (is_love_scene):
                return CheckLustSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
            else:
                return CheckSubmissionSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
        def show_public_hair(self, partner_stats, partner_tendencies, sexual_goals, is_love_scene):
            val = show_public_hair
            if (is_love_scene):
                return CheckLustSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
            else:
                return CheckSubmissionSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
        def show_tits(self, partner_stats, partner_tendencies, sexual_goals, is_love_scene):
            val = show_tits
            if (is_love_scene):
                return CheckLustSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
            else:
                return CheckSubmissionSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
        def touches_tits_gluteus(self, partner_stats, partner_tendencies, sexual_goals, is_love_scene):
            val = touches_tits_gluteus
            if (is_love_scene):
                return CheckLustSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
            else:
                return CheckSubmissionSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
        def handjob(self, partner_stats, partner_tendencies, sexual_goals, is_love_scene):
            val = handjob
            if (is_love_scene):
                return CheckLustSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
            else:
                return CheckSubmissionSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
        def squeeze_tits_gluteus(self, partner_stats, partner_tendencies, sexual_goals, is_love_scene):
            val = squeeze_tits_gluteus
            if (is_love_scene):
                return CheckLustSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
            else:
                return CheckSubmissionSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
        def titsjob(self, partner_stats, partner_tendencies, sexual_goals, is_love_scene):
            val = titsjob
            if (is_love_scene):
                return CheckLustSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
            else:
                return CheckSubmissionSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
        def oraljob(self, partner_stats, partner_tendencies, sexual_goals, is_love_scene):
            val = oraljob
            if (is_love_scene):
                return CheckLustSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
            else:
                return CheckSubmissionSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
        def show_pussy(self, partner_stats, partner_tendencies, sexual_goals, is_love_scene):
            val = show_pussy
            if (is_love_scene):
                return CheckLustSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
            else:
                return CheckSubmissionSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
        def rub_pussy(self, partner_stats, partner_tendencies, sexual_goals, is_love_scene):
            val = rub_pussy
            if (is_love_scene):
                return CheckLustSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
            else:
                return CheckSubmissionSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
        def finger_pussy(self, partner_stats, partner_tendencies, sexual_goals, is_love_scene):
            val = finger_pussy
            if (is_love_scene):
                return CheckLustSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
            else:
                return CheckSubmissionSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
        def ass_job(self, partner_stats, partner_tendencies, sexual_goals, is_love_scene):
            val = ass_job
            if (is_love_scene):
                return CheckLustSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
            else:
                return CheckSubmissionSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
        def sex_vaginal(self, partner_stats, partner_tendencies, sexual_goals, is_love_scene):
            val = sex_vaginal
            if (is_love_scene):
                return CheckLustSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
            else:
                return CheckSubmissionSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
        def finger_ass(self, partner_stats, partner_tendencies, sexual_goals, is_love_scene):
            val = finger_ass
            if (is_love_scene):
                return CheckLustSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
            else:
                return CheckSubmissionSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
        def sex_anal(self, partner_stats, partner_tendencies, sexual_goals, is_love_scene):
            val = sex_anal
            if (is_love_scene):
                return CheckLustSex(val, partner_stats, partner_tendencies, sexual_goals, 100)
            else:
                return CheckSubmissionSex(val, partner_stats, partner_tendencies, sexual_goals, 100)

define check_sex = CheckSex()

# it is possible to create other types of sex such as (for example CheckDrunkSex ()), using the functions of CheckSex (), but changing the difficulty of the scene
    # CheckDrunkSex():
    #     def sex(self, partner_stats, partner_tendencies, sexual_goals, is_love_scene):
    #         if (partner_stats.is_addicted_alcohol):
    #             difficulty = 90
    #             return check_sex.CheckSubmissionSex(sex_vaginal, partner_stats, partner_tendencies, sexual_goals, difficulty)
    #         elif (partner_stats.is_addicted_soft_drugs):
    #             difficulty = 80
    #             return check_sex.CheckSubmissionSex(sex_vaginal, partner_stats, partner_tendencies, sexual_goals, difficulty)
    #         elif (partner_stats.is_addicted_hard_drugs):
    #             difficulty = 70
    #             return check_sex.CheckSubmissionSex(sex_vaginal, partner_stats, partner_tendencies, sexual_goals, difficulty)
    #         else: 
    #             return False
