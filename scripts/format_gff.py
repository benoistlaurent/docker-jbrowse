
"""Rewrite a GFF so that the parents are define prior to the children"""

class Attributes:
    VALID_ATTRIBUTES = ['ID', 'Name', 'Alias', 'Parent', 'Target', 'Gap',
                        'Derives_from', 'Note', 'Dbxref', 'Ontology_term',
                        'Is_circular']

    def __init__(self, **kwargs):
        self._parent = []
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        attrs = ', '.join('{}={!r}'.format(key, value)
                          for key, value in self.__dict__.items())
        return "{}({})".format(type(self).__name__, attrs)

    @property
    def Parent(self):
        return self._parent

    @Parent.setter
    def Parent(self, value):
        self._parent = value.split(',')

    @classmethod
    def fromgff(cls, s):
        tokens = [tok.split('=') for tok in s.strip().split(';')]
        tokens = [tok for tok in tokens if len(tok) == 2]
        attrs = {key.strip(): value for key, value in tokens}
        return cls(**attrs)

    def togff(self):
        attrs = []
        attr_names = self.VALID_ATTRIBUTES[:]
        attr_names += [name for name in vars(self).keys()
                       if name not in attr_names and not name.startswith('_')]
        for name in attr_names:
            if hasattr(self, name):
                value = getattr(self, name)
                if isinstance(value, (list, tuple)):
                    value = ','.join(value)
                # Ignore empty attributes.
                value = str(value)
                if value.strip():
                    attrs.append((name, value))
        return ';'.join('{}={}'.format(k, v) for k, v in attrs)


class Feature:
    def __init__(self, seqid='', source='', type='', start=0, end=0, score=0.0,
                 strand='+', phase=0, attrs=Attributes()):
        self.seqid = seqid
        self.source = source
        self.type = type
        self.start = start
        self.end = end
        self.score = score
        self._strand = ''
        self._phase = ''
        self.attrs = attrs

        self.strand = strand
        self.phase = phase

    def __str__(self):
        attrs_names = ('seqid', 'source', 'type', 'start', 'end', 'score',
                       'strand', 'phase', 'attrs')
        attrs = ', '.join('{}={!r}'.format(key, getattr(self, key))
                          for key in attrs_names)
        return "{}({})".format(type(self).__name__, attrs)

    @property
    def strand(self):
        return self._strand

    @strand.setter
    def strand(self, value):
        assert value in ('+', '-')
        self._strand = value

    @property
    def phase(self):
        return self._phase

    @phase.setter
    def phase(self, value):
        # self._phase = 0 if value  ==  '.' else int(value)
        self._phase = value

    @classmethod
    def fromgff(cls, line):
        feat = cls()
        tokens = line.split('\t')
        assert len(tokens) == 9
        strand = tokens[6]

        feat.seqid = tokens[0]
        feat.source = tokens[1]
        feat.type = tokens[2]
        feat.start = int(tokens[3])
        feat.end = int(tokens[4])
        feat.score = '.'
        feat.strand = strand
        feat.phase = tokens[7]
        feat.attrs = Attributes.fromgff(tokens[8])
        return feat

    def pprint(self):
        attrs_names = ('seqid', 'source', 'type', 'start', 'end', 'score',
                       'strand', 'phase', 'attrs')
        s = type(self).__name__ + '('
        sep = ',\n{}'.format(' ' * len(s))
        s += sep.join('{}={!r}'.format(key, getattr(self, key))
                      for key in attrs_names)
        s += ')'
        print(s)

    def has_parent(self):
        return len(self.attrs.Parent) > 0

    def togff(self):
        """Format the feature as a GFF string."""
        colnames = ('seqid', 'source', 'type', 'start', 'end', 'score',
                    'strand', 'phase')
        s = '\t'.join(str(getattr(self, name)) for name in colnames)
        s += '\t' + self.attrs.togff()
        return s


class GFF:
    def __init__(self, features=[]):
        self.features = features

    def __iter__(self):
        return iter(self.features)

    @classmethod
    def fromfile(cls, path):
        features = []
        with open(path, 'rt') as f:
            for lineid, line in enumerate(f):
                if not line.startswith('#'):
                    features.append(Feature.fromgff(line))
        return cls(features)

    def duplicates(self):
        """Return features which have the same 'ID' attribute."""
        dup = {feature.attrs.ID: [] for feature in self.features}
        for feature in self.features:
            dup[feature.attrs.ID].append(feature)
        return dup

    def show_duplicates(self):
        """Print features which have the same 'ID' attribute."""
        dup = self.duplicates()
        for featid, feature_list in dup.items():
            if len(feature_list) > 1:
                print("{}:".format(featid))
                for feat in feature_list:
                    print('  ', end='')
                    feat.pprint()
                print()

    def get_feature_by_id(self, idtag):
        """Return the list of features which attribute 'ID' is `idtag`."""
        return [feature for feature in self.features
                if feature.attrs.ID == idtag]

    def get_parent(self, feature):
        """Return the list of features which attribute 'ID' corresponds to
        feature 'Parent' attribute."""
        parentid = feature.attrs.Parent
        return [feat for pid in parentid
                for feat in self.get_feature_by_id(pid)]

    def togff(self):
        def parent_to_gff(feature):
            s = ''
            if feature.has_parent():
                parent = self.get_parent(feature)
                if len(parent) > 0:
                    for p in parent:
                        s += parent_to_gff(p)
                        if p not in isdisplayed:
                            s += '\n' + p.togff()
                            isdisplayed.append(p)
                else:
                    # Remove parent is parent not found.
                    feature.attrs.Parent = ''
            return s


        s = '##gff-version 3\n'
        s += '##sequence-region cv11 1  205712'
        isdisplayed = []
        for feature in self:
            s += parent_to_gff(feature)
            if feature not in isdisplayed:
                s += '\n' + feature.togff()
                isdisplayed.append(feature)
        return s


def main():
    gfffile = 'data/cv11/cv11.gff3'
    gff = GFF.fromfile(gfffile)
    print(gff.togff())


if __name__ == '__main__':
    main()
