init python:
    ## Sexual goals
    class SexualGoals():
        def __init__(self, virgin):
            self.tongue_kiss = False
            self.tits_see = False
            self.tits_touch = False
            self.pussy_see = False
            self.pussy_touch = False
            self.virgin = virgin
            self.handjob = 0
            self.titjob = 0
            self.oraljob = 0
            self.vaginal_sex = 0
            self.anal_sex = 0
        def add_tongue_kiss(self):
            self.tongue_kiss = True
        def add_tits_see(self):
            self.tits_see = True
        def add_tits_touch(self):
            self.tits_touch = True
        def add_pussy_see(self):
            self.pussy_see = True
        def add_pussy_touch(self):
            self.pussy_touch = True
        def add_handjob(self):
            self.handjob += 1
        def add_titjob(self):
            self.titjob += 1
        def add_oraljob(self):
            self.oraljob += 1
        def add_vaginal_sex(self):
            self.vaginal_sex += 1
        def add_anal_sex(self):
            self.anal_sex += 1
        def have_tongue_kiss(self):
            return self.tongue_kiss
        def have_tits_see(self):
            return self.tits_see
        def have_tits_touch(self):
            return self.tits_touch
        def have_pussy_see(self):
            return self.pussy_see
        def have_pussy_touch(self):
            return self.pussy_touch
        def have_handjob(self):
            return self.handjob > 0
        def have_titjob(self):
            return self.titjob > 0
        def have_oraljob(self):
            return self.oraljob > 0
        def have_vaginal_sex(self):
            return self.vaginal_sex > 0
        def have_anal_sex(self):
            return self.anal_sex > 0
        def is_vaginal_virgin(self):
            return (self.virgin == 0 or virgin == True)
    ## Pregnant Goals
    class PregnantGoals():
        def __init__(self):
            self.creampie_pussy = 0
            self.pregnant = 0
            self.sons = 0
        def add_creampie_pussy(self):
            self.creampie_pussy += 1
        def add_pregnant(self):
            self.pregnant += 1
        def add_sons(self):
            self.sons += 1
        def have_creampie_pussy(self):
            return self.creampie_pussy > 0
        def have_pregnant(self):
            return self.pregnant > 0
        def have_sons(self):
            return self.sons > 0
    ## Group sex goals
    class GroupSexGoals():
        def __init__(self):
            self.lesbo_sex = 0
            self.FFM = 0
            self.NTR = 0
            self.FMM = 0
            self.Group = 0
        def add_lesbo_sex(self):
            self.lesbo_sex += 1
        def add_FFM(self):
            self.FFM += 1
        def add_NTR(self):
            self.NTR += 1
        def add_FMM(self):
            self.FMM += 1
        def add_Group(self):
            self.Group += 1
        def have_lesbo_sex(self):
            return self.lesbo_sex > 0
        def have_FFM(self):
            return self.FFM > 0
        def have_NTR(self):
            return self.NTR > 0
        def have_FMM(self):
            return self.FMM > 0
        def have_Group(self):
            return self.Group > 0
