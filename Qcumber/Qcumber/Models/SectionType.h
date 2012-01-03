//
//  SectionType.h
//  Qcumber
//
//  Created by Chris Cooper on 12-01-01.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <CoreData/CoreData.h>

@class Section;

@interface SectionType : NSManagedObject

@property (nonatomic, strong) NSString * abbreviation;
@property (nonatomic, strong) NSString * name;
@property (nonatomic, strong) NSSet *sections;
@end

@interface SectionType (CoreDataGeneratedAccessors)

- (void)addSectionsObject:(Section *)value;
- (void)removeSectionsObject:(Section *)value;
- (void)addSections:(NSSet *)values;
- (void)removeSections:(NSSet *)values;

@end
