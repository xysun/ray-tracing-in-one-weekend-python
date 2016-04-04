__author__ = 'jsun'

from hitable import Hitable
from hit_record import Hit_record
from vec3 import Vec3

class Hitable_list(Hitable):
    def __init__(self, hitables):
        self.hitables = hitables

    def hit(self, ray, t_min, t_max, hit_record):
        hit_anything = False
        closest_hit_so_far = t_max
        tmp_rec = Hit_record(t=0, p=Vec3(0,0,0), normal=Vec3(0,0,0))

        for hitable in self.hitables:
            if hitable.hit(ray, t_min, closest_hit_so_far, tmp_rec):
                hit_anything = True
                closest_hit_so_far = tmp_rec.t
                hit_record.t = tmp_rec.t
                hit_record.p = tmp_rec.p
                hit_record.normal = tmp_rec.normal
                hit_record.material = tmp_rec.material

        return hit_anything