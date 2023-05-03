import unittest

from tests.support.fake_volumes import make_fake_volumes_from


class Test_create_fake_volume_of(unittest.TestCase):

    def test_return_the_containing_volume(self):
        self.volumes = make_fake_volumes_from(['/fake-vol'])

        assert '/fake-vol' == self.volumes.volume_of('/fake-vol/foo')

    def test_with_file_that_are_outside(self):
        self.volumes = make_fake_volumes_from(['/fake-vol'])

        assert '/' == self.volumes.volume_of('/foo')

    def test_it_work_also_with_relative_mount_point(self):
        self.volumes = make_fake_volumes_from(['relative-fake-vol'])

        assert 'relative-fake-vol' == self.volumes.volume_of('relative-fake-vol/foo')
